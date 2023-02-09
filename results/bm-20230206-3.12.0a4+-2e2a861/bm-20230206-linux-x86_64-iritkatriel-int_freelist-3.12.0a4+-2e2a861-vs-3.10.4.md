
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 2e2a861
- commit date: 2023-02-06
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.35 ms: 1.40x faster                                               |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.27x faster                                              |
| html5lib       | 85.8 ms                                                | 60.3 ms: 1.42x faster                                               |
| tornado_http   | 128 ms                                                 | 93.9 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.2 ms: 1.47x faster                                               |
| nbody          | 136 ms                                                 | 95.9 ms: 1.42x faster                                               |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.25x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.11x faster                                               |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.51 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 285 us: 1.59x faster                                                |
| unpickle_pure_python | 297 us                                                 | 200 us: 1.48x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.34 ms: 1.44x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.39x faster                                               |
| json_loads           | 28.9 us                                                | 23.5 us: 1.23x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 77.5 ms: 1.20x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| pickle_list          | 4.50 us                                                | 4.22 us: 1.07x faster                                               |
| pickle_dict          | 28.3 us                                                | 31.5 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.96 ms: 1.56x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.49 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.46 ms: 1.51x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                               |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                               |
| genshi_xml      | 63.6 ms                                                | 46.5 ms: 1.37x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.21 ms: 2.30x faster                                               |
| logging_silent          | 173 ns                                                 | 92.2 ns: 1.88x faster                                               |
| scimark_sor             | 193 ms                                                 | 106 ms: 1.82x faster                                                |
| pyflate                 | 675 ms                                                 | 395 ms: 1.71x faster                                                |
| richards                | 71.4 ms                                                | 42.6 ms: 1.68x faster                                               |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                |
| raytrace                | 461 ms                                                 | 284 ms: 1.63x faster                                                |
| chaos                   | 104 ms                                                 | 64.9 ms: 1.60x faster                                               |
| pickle_pure_python      | 453 us                                                 | 285 us: 1.59x faster                                                |
| scimark_monte_carlo     | 105 ms                                                 | 66.6 ms: 1.57x faster                                               |
| hexiom                  | 9.42 ms                                                | 6.02 ms: 1.56x faster                                               |
| python_startup          | 13.9 ms                                                | 8.96 ms: 1.56x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 75.7 ms: 1.55x faster                                               |
| spectral_norm           | 148 ms                                                 | 95.5 ms: 1.55x faster                                               |
| mako                    | 14.3 ms                                                | 9.46 ms: 1.51x faster                                               |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                                |
| unpickle_pure_python    | 297 us                                                 | 200 us: 1.48x faster                                                |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                               |
| float                   | 108 ms                                                 | 73.2 ms: 1.47x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.36 sec: 1.45x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.34 ms: 1.44x faster                                               |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                               |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                               |
| html5lib                | 85.8 ms                                                | 60.3 ms: 1.42x faster                                               |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                               |
| nbody                   | 136 ms                                                 | 95.9 ms: 1.42x faster                                               |
| logging_simple          | 8.06 us                                                | 5.69 us: 1.42x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 666 ms: 1.42x faster                                                |
| logging_format          | 8.92 us                                                | 6.32 us: 1.41x faster                                               |
| chameleon               | 8.86 ms                                                | 6.35 ms: 1.40x faster                                               |
| thrift                  | 1.03 ms                                                | 740 us: 1.39x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.39x faster                                               |
| unpack_sequence         | 59.5 ns                                                | 42.8 ns: 1.39x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.96 ms: 1.39x faster                                               |
| scimark_fft             | 414 ms                                                 | 302 ms: 1.37x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 624 ms: 1.37x faster                                                |
| tornado_http            | 128 ms                                                 | 93.9 ms: 1.37x faster                                               |
| genshi_xml              | 63.6 ms                                                | 46.5 ms: 1.37x faster                                               |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| aiohttp                 | 1.34 ms                                                | 994 us: 1.34x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| pycparser               | 1.51 sec                                               | 1.14 sec: 1.32x faster                                              |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| fannkuch                | 477 ms                                                 | 363 ms: 1.31x faster                                                |
| coroutines              | 31.7 ms                                                | 24.5 ms: 1.29x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| deepcopy                | 429 us                                                 | 334 us: 1.29x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.27x faster                                              |
| nqueens                 | 99.3 ms                                                | 78.1 ms: 1.27x faster                                               |
| deepcopy_reduce         | 3.75 us                                                | 2.97 us: 1.26x faster                                               |
| mypy                    | 1.01 sec                                               | 806 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed | 949 ms                                                 | 757 ms: 1.25x faster                                                |
| json_loads              | 28.9 us                                                | 23.5 us: 1.23x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 19.7 ms: 1.22x faster                                               |
| async_generators        | 428 ms                                                 | 352 ms: 1.21x faster                                                |
| bench_thread_pool       | 943 us                                                 | 779 us: 1.21x faster                                                |
| dulwich_log             | 75.5 ms                                                | 62.4 ms: 1.21x faster                                               |
| xml_etree_generate      | 93.3 ms                                                | 77.5 ms: 1.20x faster                                               |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                |
| json                    | 5.35 ms                                                | 4.50 ms: 1.19x faster                                               |
| sympy_expand            | 537 ms                                                 | 456 ms: 1.18x faster                                                |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.17x faster                                                |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.15x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.11x faster                                               |
| sqlite_synth            | 2.90 us                                                | 2.61 us: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                               |
| telco                   | 6.68 ms                                                | 6.17 ms: 1.08x faster                                               |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| pickle_list             | 4.50 us                                                | 4.22 us: 1.07x faster                                               |
| mdp                     | 2.82 sec                                               | 2.65 sec: 1.07x faster                                              |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                |
| generators              | 75.8 ms                                                | 78.7 ms: 1.04x slower                                               |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| regex_effbot            | 3.21 ms                                                | 3.51 ms: 1.09x slower                                               |
| pickle_dict             | 28.3 us                                                | 31.5 us: 1.11x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.49 ms: 1.13x slower                                               |
| coverage                | 75.3 ms                                                | 96.8 ms: 1.28x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, pickle
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230206-3.12.0a4+-2e2a861/bm-20230206-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-2e2a861.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
