
# Results vs. 3.10.4

- fork: faster-cpython
- ref: normalize_current_ex
- machine: linux-x86_64
- commit hash: 0c3dc7b
- commit date: 2023-02-06
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.34x faster                                                             |
| chameleon      | 9.17 ms                                                | 6.51 ms: 1.41x faster                                                            |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                           |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.40x faster                                                            |
| tornado_http   | 128 ms                                                 | 94.4 ms: 1.36x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.6 ms: 1.52x faster                                                            |
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                            |
| regex_dna      | 214 ms                                                 | 206 ms: 1.04x faster                                                             |
| regex_effbot   | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 284 us: 1.59x faster                                                             |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                             |
| json_dumps           | 13.4 ms                                                | 9.44 ms: 1.42x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 55.2 ms: 1.35x faster                                                            |
| json_loads           | 28.7 us                                                | 23.8 us: 1.21x faster                                                            |
| xml_etree_generate   | 93.8 ms                                                | 79.7 ms: 1.18x faster                                                            |
| pickle_list          | 4.72 us                                                | 4.25 us: 1.11x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.08x faster                                                             |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                            |
| pickle_dict          | 27.6 us                                                | 32.0 us: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                     |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.95 ms: 1.57x faster                                                            |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.67 ms: 1.52x faster                                                            |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                            |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                            |
| genshi_xml      | 63.7 ms                                                | 46.7 ms: 1.36x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.20 ms: 2.27x faster                                                            |
| logging_silent          | 176 ns                                                 | 93.2 ns: 1.89x faster                                                            |
| asyncio_tcp             | 914 ms                                                 | 493 ms: 1.85x faster                                                             |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                             |
| richards                | 75.2 ms                                                | 42.1 ms: 1.78x faster                                                            |
| pyflate                 | 676 ms                                                 | 398 ms: 1.70x faster                                                             |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 64.7 ms: 1.68x faster                                                            |
| chaos                   | 106 ms                                                 | 63.4 ms: 1.66x faster                                                            |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                                             |
| crypto_pyaes            | 117 ms                                                 | 72.8 ms: 1.60x faster                                                            |
| pickle_pure_python      | 452 us                                                 | 284 us: 1.59x faster                                                             |
| hexiom                  | 9.43 ms                                                | 5.97 ms: 1.58x faster                                                            |
| python_startup          | 14.1 ms                                                | 8.95 ms: 1.57x faster                                                            |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                             |
| nbody                   | 144 ms                                                 | 94.6 ms: 1.52x faster                                                            |
| mako                    | 14.7 ms                                                | 9.67 ms: 1.52x faster                                                            |
| deepcopy_memo           | 51.7 us                                                | 34.3 us: 1.51x faster                                                            |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                                            |
| scimark_lu              | 161 ms                                                 | 109 ms: 1.48x faster                                                             |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                            |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.44 ms: 1.42x faster                                                            |
| unpack_sequence         | 59.4 ns                                                | 41.7 ns: 1.42x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                           |
| sqlglot_transpile       | 2.43 ms                                                | 1.72 ms: 1.41x faster                                                            |
| chameleon               | 9.17 ms                                                | 6.51 ms: 1.41x faster                                                            |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.40x faster                                                            |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 689 ms: 1.38x faster                                                             |
| scimark_fft             | 421 ms                                                 | 305 ms: 1.38x faster                                                             |
| logging_simple          | 8.10 us                                                | 5.88 us: 1.38x faster                                                            |
| pycparser               | 1.53 sec                                               | 1.11 sec: 1.38x faster                                                           |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                             |
| thrift                  | 1.03 ms                                                | 757 us: 1.37x faster                                                             |
| logging_format          | 8.85 us                                                | 6.48 us: 1.37x faster                                                            |
| genshi_xml              | 63.7 ms                                                | 46.7 ms: 1.36x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                                            |
| tornado_http            | 128 ms                                                 | 94.4 ms: 1.36x faster                                                            |
| xml_etree_process       | 74.5 ms                                                | 55.2 ms: 1.35x faster                                                            |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                           |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 639 ms: 1.34x faster                                                             |
| 2to3                    | 335 ms                                                 | 251 ms: 1.34x faster                                                             |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                             |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                                            |
| fannkuch                | 488 ms                                                 | 368 ms: 1.32x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 2.90 us: 1.30x faster                                                            |
| nqueens                 | 100 ms                                                 | 76.9 ms: 1.30x faster                                                            |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.29x faster                                                            |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                             |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                           |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                                             |
| coroutines              | 31.6 ms                                                | 25.4 ms: 1.25x faster                                                            |
| json_loads              | 28.7 us                                                | 23.8 us: 1.21x faster                                                            |
| sympy_integrate         | 24.0 ms                                                | 20.0 ms: 1.20x faster                                                            |
| bench_thread_pool       | 946 us                                                 | 787 us: 1.20x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 63.1 ms: 1.20x faster                                                            |
| sympy_str               | 325 ms                                                 | 272 ms: 1.19x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 79.7 ms: 1.18x faster                                                            |
| json                    | 5.35 ms                                                | 4.57 ms: 1.17x faster                                                            |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                                             |
| sympy_expand            | 534 ms                                                 | 459 ms: 1.16x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                            |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                                            |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.12x faster                                                            |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.12x faster                                                            |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                            |
| pickle_list             | 4.72 us                                                | 4.25 us: 1.11x faster                                                            |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                             |
| mdp                     | 2.74 sec                                               | 2.51 sec: 1.09x faster                                                           |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.08x faster                                                             |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                            |
| telco                   | 6.73 ms                                                | 6.38 ms: 1.06x faster                                                            |
| regex_dna               | 214 ms                                                 | 206 ms: 1.04x faster                                                             |
| async_generators        | 426 ms                                                 | 424 ms: 1.00x faster                                                             |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| regex_effbot            | 3.19 ms                                                | 3.36 ms: 1.05x slower                                                            |
| gc_traversal            | 3.53 ms                                                | 3.82 ms: 1.08x slower                                                            |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                                            |
| dask                    | 436 ms                                                 | 500 ms: 1.15x slower                                                             |
| pickle_dict             | 27.6 us                                                | 32.0 us: 1.16x slower                                                            |
| coverage                | 74.7 ms                                                | 96.5 ms: 1.29x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                     |

Benchmark hidden because not significant (4): bench_mp_pool, generators, pickle, unpickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230206-3.12.0a4+-0c3dc7b/bm-20230206-linux-x86_64-faster%2dcpython-normalize_current_ex-3.12.0a4+-0c3dc7b.json: mypy
