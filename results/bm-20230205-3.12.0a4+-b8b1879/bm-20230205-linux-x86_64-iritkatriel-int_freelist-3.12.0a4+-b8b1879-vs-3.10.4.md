
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b8b1879
- commit date: 2023-02-05
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| chameleon      | 9.17 ms                                                | 6.34 ms: 1.44x faster                                               |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                               |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 109 ms                                                 | 72.9 ms: 1.49x faster                                               |
| nbody          | 144 ms                                                 | 99.5 ms: 1.45x faster                                               |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                  | 1.29x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                               |
| regex_dna      | 214 ms                                                 | 214 ms: 1.00x slower                                                |
| regex_effbot   | 3.19 ms                                                | 3.62 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                               |
| json_loads           | 28.7 us                                                | 23.5 us: 1.22x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 78.1 ms: 1.20x faster                                               |
| pickle_list          | 4.72 us                                                | 4.00 us: 1.18x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| unpickle_list        | 4.92 us                                                | 4.84 us: 1.02x faster                                               |
| pickle               | 10.2 us                                                | 9.98 us: 1.02x faster                                               |
| pickle_dict          | 27.6 us                                                | 30.1 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.92 ms: 1.58x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.46 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.62 ms: 1.52x faster                                               |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.45x faster                                               |
| django_template | 46.3 ms                                                | 32.5 ms: 1.43x faster                                               |
| genshi_xml      | 63.7 ms                                                | 47.7 ms: 1.34x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                               |
| logging_silent          | 176 ns                                                 | 92.6 ns: 1.90x faster                                               |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 493 ms: 1.85x faster                                                |
| richards                | 75.2 ms                                                | 42.4 ms: 1.77x faster                                               |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                                |
| pyflate                 | 676 ms                                                 | 401 ms: 1.68x faster                                                |
| chaos                   | 106 ms                                                 | 63.2 ms: 1.67x faster                                               |
| raytrace                | 467 ms                                                 | 287 ms: 1.63x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 67.7 ms: 1.60x faster                                               |
| python_startup          | 14.1 ms                                                | 8.92 ms: 1.58x faster                                               |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                |
| hexiom                  | 9.43 ms                                                | 5.98 ms: 1.58x faster                                               |
| spectral_norm           | 150 ms                                                 | 95.0 ms: 1.57x faster                                               |
| crypto_pyaes            | 117 ms                                                 | 75.2 ms: 1.55x faster                                               |
| mako                    | 14.7 ms                                                | 9.62 ms: 1.52x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                |
| float                   | 109 ms                                                 | 72.9 ms: 1.49x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 34.7 us: 1.49x faster                                               |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.47x faster                                                |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                               |
| nbody                   | 144 ms                                                 | 99.5 ms: 1.45x faster                                               |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.45x faster                                               |
| chameleon               | 9.17 ms                                                | 6.34 ms: 1.44x faster                                               |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                               |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                               |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.43x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                              |
| logging_simple          | 8.10 us                                                | 5.76 us: 1.41x faster                                               |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.92 ms: 1.39x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                                |
| logging_format          | 8.85 us                                                | 6.38 us: 1.39x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| unpack_sequence         | 59.4 ns                                                | 43.2 ns: 1.38x faster                                               |
| scimark_fft             | 421 ms                                                 | 309 ms: 1.37x faster                                                |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                               |
| pycparser               | 1.53 sec                                               | 1.13 sec: 1.36x faster                                              |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                                |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                              |
| genshi_xml              | 63.7 ms                                                | 47.7 ms: 1.34x faster                                               |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                |
| fannkuch                | 488 ms                                                 | 367 ms: 1.33x faster                                                |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| deepcopy                | 438 us                                                 | 336 us: 1.30x faster                                                |
| nqueens                 | 100 ms                                                 | 77.0 ms: 1.30x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 659 ms: 1.30x faster                                                |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                |
| sqlglot_optimize        | 65.2 ms                                                | 51.3 ms: 1.27x faster                                               |
| coroutines              | 31.6 ms                                                | 24.9 ms: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| deepcopy_reduce         | 3.79 us                                                | 3.01 us: 1.26x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 762 ms: 1.25x faster                                                |
| json_loads              | 28.7 us                                                | 23.5 us: 1.22x faster                                               |
| async_generators        | 426 ms                                                 | 349 ms: 1.22x faster                                                |
| dulwich_log             | 75.8 ms                                                | 62.4 ms: 1.22x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 19.8 ms: 1.21x faster                                               |
| bench_thread_pool       | 946 us                                                 | 780 us: 1.21x faster                                                |
| xml_etree_generate      | 93.8 ms                                                | 78.1 ms: 1.20x faster                                               |
| sympy_str               | 325 ms                                                 | 272 ms: 1.19x faster                                                |
| pickle_list             | 4.72 us                                                | 4.00 us: 1.18x faster                                               |
| json                    | 5.35 ms                                                | 4.55 ms: 1.18x faster                                               |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.17x faster                                                |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                |
| sqlite_synth            | 2.92 us                                                | 2.55 us: 1.15x faster                                               |
| create_gc_cycles        | 1.65 ms                                                | 1.45 ms: 1.14x faster                                               |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| mdp                     | 2.74 sec                                               | 2.49 sec: 1.10x faster                                              |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                               |
| telco                   | 6.73 ms                                                | 6.42 ms: 1.05x faster                                               |
| unpickle_list           | 4.92 us                                                | 4.84 us: 1.02x faster                                               |
| pickle                  | 10.2 us                                                | 9.98 us: 1.02x faster                                               |
| regex_dna               | 214 ms                                                 | 214 ms: 1.00x slower                                                |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x slower                                                |
| gc_traversal            | 3.53 ms                                                | 3.76 ms: 1.06x slower                                               |
| pickle_dict             | 27.6 us                                                | 30.1 us: 1.09x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.46 ms: 1.12x slower                                               |
| regex_effbot            | 3.19 ms                                                | 3.62 ms: 1.13x slower                                               |
| dask                    | 436 ms                                                 | 497 ms: 1.14x slower                                                |
| coverage                | 74.7 ms                                                | 98.9 ms: 1.32x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (2): bench_mp_pool, generators
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230205-3.12.0a4+-b8b1879/bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879.json: mypy
