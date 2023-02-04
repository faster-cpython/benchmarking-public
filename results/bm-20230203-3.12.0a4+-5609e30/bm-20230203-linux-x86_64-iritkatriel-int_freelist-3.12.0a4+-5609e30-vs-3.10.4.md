
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 5609e30
- commit date: 2023-02-03
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.26 ms: 1.42x faster                                               |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.8 ms                                                | 59.6 ms: 1.44x faster                                               |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.3 ms: 1.49x faster                                               |
| nbody          | 136 ms                                                 | 96.5 ms: 1.41x faster                                               |
| pidigits       | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.28x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.48 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 281 us: 1.61x faster                                                |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.50x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.27 ms: 1.45x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                               |
| json_loads           | 28.9 us                                                | 23.4 us: 1.23x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 77.7 ms: 1.20x faster                                               |
| unpickle             | 14.3 us                                                | 12.7 us: 1.12x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| pickle_list          | 4.50 us                                                | 4.08 us: 1.10x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 101 ms: 1.09x faster                                                |
| pickle               | 10.1 us                                                | 10.0 us: 1.01x faster                                               |
| unpickle_list        | 4.99 us                                                | 4.96 us: 1.01x faster                                               |
| pickle_dict          | 28.3 us                                                | 30.4 us: 1.07x slower                                               |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.97 ms: 1.55x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.50 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.48 ms: 1.50x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                               |
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.3 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.19 ms: 2.32x faster                                               |
| logging_silent          | 173 ns                                                 | 91.5 ns: 1.89x faster                                               |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.83x faster                                                |
| pyflate                 | 675 ms                                                 | 398 ms: 1.70x faster                                                |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                |
| richards                | 71.4 ms                                                | 42.5 ms: 1.68x faster                                               |
| raytrace                | 461 ms                                                 | 284 ms: 1.62x faster                                                |
| chaos                   | 104 ms                                                 | 64.2 ms: 1.62x faster                                               |
| pickle_pure_python      | 453 us                                                 | 281 us: 1.61x faster                                                |
| scimark_monte_carlo     | 105 ms                                                 | 66.5 ms: 1.58x faster                                               |
| hexiom                  | 9.42 ms                                                | 6.02 ms: 1.56x faster                                               |
| python_startup          | 13.9 ms                                                | 8.97 ms: 1.55x faster                                               |
| spectral_norm           | 148 ms                                                 | 95.7 ms: 1.55x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.6 ms: 1.53x faster                                               |
| mako                    | 14.3 ms                                                | 9.48 ms: 1.50x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.50x faster                                                |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                                |
| float                   | 108 ms                                                 | 72.3 ms: 1.49x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.27 ms: 1.45x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                               |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                               |
| html5lib                | 85.8 ms                                                | 59.6 ms: 1.44x faster                                               |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                               |
| logging_format          | 8.92 us                                                | 6.24 us: 1.43x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                              |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                               |
| logging_simple          | 8.06 us                                                | 5.68 us: 1.42x faster                                               |
| chameleon               | 8.86 ms                                                | 6.26 ms: 1.42x faster                                               |
| nbody                   | 136 ms                                                 | 96.5 ms: 1.41x faster                                               |
| thrift                  | 1.03 ms                                                | 736 us: 1.40x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                                |
| unpack_sequence         | 59.5 ns                                                | 42.9 ns: 1.39x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.98 ms: 1.38x faster                                               |
| scimark_fft             | 414 ms                                                 | 303 ms: 1.37x faster                                                |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                               |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| async_tree_none         | 713 ms                                                 | 527 ms: 1.35x faster                                                |
| aiohttp                 | 1.34 ms                                                | 989 us: 1.35x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.34x faster                                               |
| genshi_xml              | 63.6 ms                                                | 47.3 ms: 1.34x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                              |
| pycparser               | 1.51 sec                                               | 1.13 sec: 1.33x faster                                              |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 653 ms: 1.31x faster                                                |
| fannkuch                | 477 ms                                                 | 371 ms: 1.29x faster                                                |
| deepcopy                | 429 us                                                 | 335 us: 1.28x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| nqueens                 | 99.3 ms                                                | 78.4 ms: 1.27x faster                                               |
| coroutines              | 31.7 ms                                                | 25.0 ms: 1.27x faster                                               |
| deepcopy_reduce         | 3.75 us                                                | 2.97 us: 1.26x faster                                               |
| mypy                    | 1.01 sec                                               | 805 ms: 1.26x faster                                                |
| async_tree_cpu_io_mixed | 949 ms                                                 | 759 ms: 1.25x faster                                                |
| json_loads              | 28.9 us                                                | 23.4 us: 1.23x faster                                               |
| bench_thread_pool       | 943 us                                                 | 779 us: 1.21x faster                                                |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                               |
| dulwich_log             | 75.5 ms                                                | 62.6 ms: 1.21x faster                                               |
| sympy_str               | 324 ms                                                 | 269 ms: 1.20x faster                                                |
| xml_etree_generate      | 93.3 ms                                                | 77.7 ms: 1.20x faster                                               |
| async_generators        | 428 ms                                                 | 357 ms: 1.20x faster                                                |
| json                    | 5.35 ms                                                | 4.54 ms: 1.18x faster                                               |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                |
| sympy_expand            | 537 ms                                                 | 456 ms: 1.18x faster                                                |
| sqlite_synth            | 2.90 us                                                | 2.54 us: 1.14x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.14x faster                                               |
| unpickle                | 14.3 us                                                | 12.7 us: 1.12x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| pickle_list             | 4.50 us                                                | 4.08 us: 1.10x faster                                               |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                |
| xml_etree_iterparse     | 110 ms                                                 | 101 ms: 1.09x faster                                                |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.08x faster                                              |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                |
| telco                   | 6.68 ms                                                | 6.54 ms: 1.02x faster                                               |
| pickle                  | 10.1 us                                                | 10.0 us: 1.01x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.96 us: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 191 ms: 1.00x slower                                                |
| generators              | 75.8 ms                                                | 76.5 ms: 1.01x slower                                               |
| pickle_dict             | 28.3 us                                                | 30.4 us: 1.07x slower                                               |
| regex_effbot            | 3.21 ms                                                | 3.48 ms: 1.09x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.50 ms: 1.13x slower                                               |
| coverage                | 75.3 ms                                                | 96.7 ms: 1.28x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230203-3.12.0a4+-5609e30/bm-20230203-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-5609e30.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
