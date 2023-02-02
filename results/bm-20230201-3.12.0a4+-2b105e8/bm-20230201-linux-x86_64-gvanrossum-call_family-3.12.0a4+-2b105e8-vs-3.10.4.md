
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: 2b105e8
- commit date: 2023-02-01
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.33x faster                                              |
| chameleon      | 8.86 ms                                                | 6.42 ms: 1.38x faster                                             |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                            |
| html5lib       | 85.8 ms                                                | 59.4 ms: 1.44x faster                                             |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.8 ms: 1.48x faster                                             |
| nbody          | 136 ms                                                 | 94.5 ms: 1.44x faster                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.27x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 127 ms: 1.37x faster                                              |
| regex_v8       | 25.0 ms                                                | 21.5 ms: 1.16x faster                                             |
| regex_dna      | 214 ms                                                 | 213 ms: 1.01x faster                                              |
| regex_effbot   | 3.21 ms                                                | 3.62 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 283 us: 1.60x faster                                              |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.50x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.43x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 53.3 ms: 1.40x faster                                             |
| json_loads           | 28.9 us                                                | 23.8 us: 1.22x faster                                             |
| xml_etree_generate   | 93.3 ms                                                | 77.2 ms: 1.21x faster                                             |
| pickle_list          | 4.50 us                                                | 3.99 us: 1.13x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                              |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                             |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                              |
| pickle               | 10.1 us                                                | 10.1 us: 1.01x faster                                             |
| unpickle_list        | 4.99 us                                                | 5.03 us: 1.01x slower                                             |
| pickle_dict          | 28.3 us                                                | 30.6 us: 1.08x slower                                             |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.95 ms: 1.56x faster                                             |
| python_startup_no_site | 5.76 ms                                                | 6.48 ms: 1.12x slower                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                             |
| mako            | 14.3 ms                                                | 9.73 ms: 1.46x faster                                             |
| django_template | 46.3 ms                                                | 32.1 ms: 1.44x faster                                             |
| genshi_xml      | 63.6 ms                                                | 46.2 ms: 1.38x faster                                             |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.13 ms: 2.36x faster                                             |
| logging_silent          | 173 ns                                                 | 91.1 ns: 1.90x faster                                             |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.84x faster                                              |
| pyflate                 | 675 ms                                                 | 395 ms: 1.71x faster                                              |
| richards                | 71.4 ms                                                | 41.8 ms: 1.71x faster                                             |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                              |
| chaos                   | 104 ms                                                 | 63.0 ms: 1.65x faster                                             |
| raytrace                | 461 ms                                                 | 280 ms: 1.65x faster                                              |
| pickle_pure_python      | 453 us                                                 | 283 us: 1.60x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 73.7 ms: 1.60x faster                                             |
| scimark_monte_carlo     | 105 ms                                                 | 65.9 ms: 1.59x faster                                             |
| hexiom                  | 9.42 ms                                                | 5.94 ms: 1.59x faster                                             |
| python_startup          | 13.9 ms                                                | 8.95 ms: 1.56x faster                                             |
| spectral_norm           | 148 ms                                                 | 97.2 ms: 1.52x faster                                             |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.50x faster                                              |
| scimark_lu              | 158 ms                                                 | 105 ms: 1.50x faster                                              |
| float                   | 108 ms                                                 | 72.8 ms: 1.48x faster                                             |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                             |
| mako                    | 14.3 ms                                                | 9.73 ms: 1.46x faster                                             |
| html5lib                | 85.8 ms                                                | 59.4 ms: 1.44x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                             |
| nbody                   | 136 ms                                                 | 94.5 ms: 1.44x faster                                             |
| django_template         | 46.3 ms                                                | 32.1 ms: 1.44x faster                                             |
| deepcopy_memo           | 50.0 us                                                | 34.9 us: 1.43x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.43x faster                                             |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                            |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                             |
| logging_format          | 8.92 us                                                | 6.37 us: 1.40x faster                                             |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                              |
| xml_etree_process       | 74.5 ms                                                | 53.3 ms: 1.40x faster                                             |
| unpack_sequence         | 59.5 ns                                                | 42.6 ns: 1.39x faster                                             |
| logging_simple          | 8.06 us                                                | 5.81 us: 1.39x faster                                             |
| chameleon               | 8.86 ms                                                | 6.42 ms: 1.38x faster                                             |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.38x faster                                            |
| genshi_xml              | 63.6 ms                                                | 46.2 ms: 1.38x faster                                             |
| thrift                  | 1.03 ms                                                | 751 us: 1.37x faster                                              |
| regex_compile           | 174 ms                                                 | 127 ms: 1.37x faster                                              |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                             |
| async_tree_none         | 713 ms                                                 | 526 ms: 1.35x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                            |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                              |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                             |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.13 ms: 1.33x faster                                             |
| 2to3                    | 332 ms                                                 | 251 ms: 1.33x faster                                              |
| scimark_fft             | 414 ms                                                 | 313 ms: 1.32x faster                                              |
| fannkuch                | 477 ms                                                 | 363 ms: 1.32x faster                                              |
| deepcopy                | 429 us                                                 | 329 us: 1.31x faster                                              |
| deepcopy_reduce         | 3.75 us                                                | 2.88 us: 1.30x faster                                             |
| coroutines              | 31.7 ms                                                | 24.5 ms: 1.29x faster                                             |
| async_tree_memoization  | 854 ms                                                 | 664 ms: 1.29x faster                                              |
| nqueens                 | 99.3 ms                                                | 77.3 ms: 1.29x faster                                             |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                             |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                            |
| mypy                    | 1.01 sec                                               | 806 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 754 ms: 1.26x faster                                              |
| async_generators        | 428 ms                                                 | 348 ms: 1.23x faster                                              |
| json_loads              | 28.9 us                                                | 23.8 us: 1.22x faster                                             |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.21x faster                                             |
| bench_thread_pool       | 943 us                                                 | 779 us: 1.21x faster                                              |
| xml_etree_generate      | 93.3 ms                                                | 77.2 ms: 1.21x faster                                             |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                              |
| dulwich_log             | 75.5 ms                                                | 63.3 ms: 1.19x faster                                             |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.19x faster                                              |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                              |
| regex_v8                | 25.0 ms                                                | 21.5 ms: 1.16x faster                                             |
| json                    | 5.35 ms                                                | 4.65 ms: 1.15x faster                                             |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                             |
| pickle_list             | 4.50 us                                                | 3.99 us: 1.13x faster                                             |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                              |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                              |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                             |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                            |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                              |
| telco                   | 6.68 ms                                                | 6.36 ms: 1.05x faster                                             |
| generators              | 75.8 ms                                                | 74.9 ms: 1.01x faster                                             |
| pickle                  | 10.1 us                                                | 10.1 us: 1.01x faster                                             |
| regex_dna               | 214 ms                                                 | 213 ms: 1.01x faster                                              |
| unpickle_list           | 4.99 us                                                | 5.03 us: 1.01x slower                                             |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| pickle_dict             | 28.3 us                                                | 30.6 us: 1.08x slower                                             |
| python_startup_no_site  | 5.76 ms                                                | 6.48 ms: 1.12x slower                                             |
| regex_effbot            | 3.21 ms                                                | 3.62 ms: 1.13x slower                                             |
| coverage                | 75.3 ms                                                | 97.1 ms: 1.29x slower                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230201-3.12.0a4+-2b105e8/bm-20230201-linux-x86_64-gvanrossum-call_family-3.12.0a4+-2b105e8.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
