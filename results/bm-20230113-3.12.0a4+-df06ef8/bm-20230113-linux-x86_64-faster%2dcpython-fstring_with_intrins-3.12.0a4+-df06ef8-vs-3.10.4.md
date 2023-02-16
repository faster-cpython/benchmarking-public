
# Results vs. 3.10.4

- fork: faster-cpython
- ref: fstring_with_intrins
- machine: linux-x86_64
- commit hash: df06ef8
- commit date: 2023-01-13
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.32x faster                                                             |
| chameleon      | 9.17 ms                                                | 6.37 ms: 1.44x faster                                                            |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                           |
| html5lib       | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                            |
| tornado_http   | 128 ms                                                 | 93.4 ms: 1.37x faster                                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.7 ms: 1.53x faster                                                            |
| float          | 109 ms                                                 | 72.2 ms: 1.51x faster                                                            |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                             |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                             |
| regex_effbot   | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                             |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.53x faster                                                             |
| json_dumps           | 13.4 ms                                                | 9.46 ms: 1.42x faster                                                            |
| xml_etree_process    | 74.5 ms                                                | 53.8 ms: 1.38x faster                                                            |
| xml_etree_generate   | 93.8 ms                                                | 77.5 ms: 1.21x faster                                                            |
| json_loads           | 28.7 us                                                | 24.0 us: 1.19x faster                                                            |
| pickle_list          | 4.72 us                                                | 4.10 us: 1.15x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                             |
| unpickle             | 14.2 us                                                | 13.1 us: 1.08x faster                                                            |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.05x faster                                                             |
| unpickle_list        | 4.92 us                                                | 4.97 us: 1.01x slower                                                            |
| pickle_dict          | 27.6 us                                                | 30.7 us: 1.11x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                     |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.57 ms: 1.64x faster                                                            |
| python_startup_no_site | 5.78 ms                                                | 6.13 ms: 1.06x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.75 ms: 1.50x faster                                                            |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                            |
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                            |
| genshi_xml      | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.19 ms: 2.28x faster                                                            |
| logging_silent          | 176 ns                                                 | 91.5 ns: 1.93x faster                                                            |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                             |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.81x faster                                                             |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                                            |
| pyflate                 | 676 ms                                                 | 394 ms: 1.72x faster                                                             |
| scimark_monte_carlo     | 109 ms                                                 | 64.3 ms: 1.69x faster                                                            |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                             |
| python_startup          | 14.1 ms                                                | 8.57 ms: 1.64x faster                                                            |
| raytrace                | 467 ms                                                 | 287 ms: 1.62x faster                                                             |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                             |
| hexiom                  | 9.43 ms                                                | 5.95 ms: 1.59x faster                                                            |
| chaos                   | 106 ms                                                 | 66.9 ms: 1.58x faster                                                            |
| crypto_pyaes            | 117 ms                                                 | 74.3 ms: 1.57x faster                                                            |
| deepcopy_memo           | 51.7 us                                                | 33.5 us: 1.54x faster                                                            |
| nbody                   | 144 ms                                                 | 93.7 ms: 1.53x faster                                                            |
| spectral_norm           | 150 ms                                                 | 97.6 ms: 1.53x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.53x faster                                                             |
| float                   | 109 ms                                                 | 72.2 ms: 1.51x faster                                                            |
| mako                    | 14.7 ms                                                | 9.75 ms: 1.50x faster                                                            |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.49x faster                                                            |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                            |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                           |
| chameleon               | 9.17 ms                                                | 6.37 ms: 1.44x faster                                                            |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                            |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 666 ms: 1.43x faster                                                             |
| html5lib                | 85.9 ms                                                | 60.2 ms: 1.43x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.46 ms: 1.42x faster                                                            |
| logging_simple          | 8.10 us                                                | 5.71 us: 1.42x faster                                                            |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.41x faster                                                           |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                                            |
| thrift                  | 1.03 ms                                                | 746 us: 1.39x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 53.8 ms: 1.38x faster                                                            |
| unpack_sequence         | 59.4 ns                                                | 43.0 ns: 1.38x faster                                                            |
| tornado_http            | 128 ms                                                 | 93.4 ms: 1.37x faster                                                            |
| genshi_xml              | 63.7 ms                                                | 46.5 ms: 1.37x faster                                                            |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                                            |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                                             |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                                           |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                            |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                            |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                             |
| 2to3                    | 335 ms                                                 | 253 ms: 1.32x faster                                                             |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                                             |
| deepcopy_reduce         | 3.79 us                                                | 2.89 us: 1.31x faster                                                            |
| async_tree_memoization  | 855 ms                                                 | 656 ms: 1.30x faster                                                             |
| coroutines              | 31.6 ms                                                | 24.7 ms: 1.28x faster                                                            |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                            |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 745 ms: 1.27x faster                                                             |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                           |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                            |
| dulwich_log             | 75.8 ms                                                | 61.6 ms: 1.23x faster                                                            |
| bench_thread_pool       | 946 us                                                 | 778 us: 1.22x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 77.5 ms: 1.21x faster                                                            |
| async_generators        | 426 ms                                                 | 355 ms: 1.20x faster                                                             |
| json_loads              | 28.7 us                                                | 24.0 us: 1.19x faster                                                            |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.19x faster                                                            |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                             |
| sympy_str               | 325 ms                                                 | 281 ms: 1.15x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                            |
| pickle_list             | 4.72 us                                                | 4.10 us: 1.15x faster                                                            |
| sqlite_synth            | 2.92 us                                                | 2.56 us: 1.14x faster                                                            |
| json                    | 5.35 ms                                                | 4.72 ms: 1.13x faster                                                            |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                            |
| djangocms               | 36.9 us                                                | 32.8 us: 1.12x faster                                                            |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                            |
| mdp                     | 2.74 sec                                               | 2.47 sec: 1.11x faster                                                           |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                             |
| unpickle                | 14.2 us                                                | 13.1 us: 1.08x faster                                                            |
| telco                   | 6.73 ms                                                | 6.24 ms: 1.08x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.05x faster                                                             |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                             |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                             |
| generators              | 76.4 ms                                                | 77.2 ms: 1.01x slower                                                            |
| unpickle_list           | 4.92 us                                                | 4.97 us: 1.01x slower                                                            |
| python_startup_no_site  | 5.78 ms                                                | 6.13 ms: 1.06x slower                                                            |
| gc_traversal            | 3.53 ms                                                | 3.79 ms: 1.07x slower                                                            |
| pickle_dict             | 27.6 us                                                | 30.7 us: 1.11x slower                                                            |
| regex_effbot            | 3.19 ms                                                | 3.58 ms: 1.12x slower                                                            |
| dask                    | 436 ms                                                 | 496 ms: 1.14x slower                                                             |
| coverage                | 74.7 ms                                                | 99.6 ms: 1.33x slower                                                            |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                     |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230113-3.12.0a4+-df06ef8/bm-20230113-linux-x86_64-faster%2dcpython-fstring_with_intrins-3.12.0a4+-df06ef8.json: mypy
