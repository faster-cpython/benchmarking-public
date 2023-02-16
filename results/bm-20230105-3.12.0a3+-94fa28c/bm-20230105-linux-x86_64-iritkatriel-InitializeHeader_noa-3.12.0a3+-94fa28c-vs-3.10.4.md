
# Results vs. 3.10.4

- fork: iritkatriel
- ref: InitializeHeader_noa
- machine: linux-x86_64
- commit hash: 94fa28c
- commit date: 2023-01-05
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 254 ms: 1.32x faster                                                        |
| chameleon      | 9.17 ms                                                | 6.15 ms: 1.49x faster                                                       |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                      |
| html5lib       | 85.9 ms                                                | 60.0 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 95.7 ms: 1.50x faster                                                       |
| float          | 109 ms                                                 | 73.0 ms: 1.49x faster                                                       |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                       |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| regex_effbot   | 3.19 ms                                                | 3.61 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 287 us: 1.58x faster                                                        |
| unpickle_pure_python | 302 us                                                 | 197 us: 1.53x faster                                                        |
| json_dumps           | 13.4 ms                                                | 9.28 ms: 1.45x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.40x faster                                                       |
| xml_etree_generate   | 93.8 ms                                                | 76.5 ms: 1.23x faster                                                       |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                                       |
| pickle_list          | 4.72 us                                                | 4.04 us: 1.17x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| unpickle             | 14.2 us                                                | 12.9 us: 1.10x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| unpickle_list        | 4.92 us                                                | 4.96 us: 1.01x slower                                                       |
| pickle_dict          | 27.6 us                                                | 31.0 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.49 ms: 1.66x faster                                                       |
| python_startup_no_site | 5.78 ms                                                | 6.08 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.38 ms: 1.56x faster                                                       |
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                                       |
| genshi_xml      | 63.7 ms                                                | 46.9 ms: 1.36x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.29 ms: 2.21x faster                                                       |
| logging_silent          | 176 ns                                                 | 92.5 ns: 1.91x faster                                                       |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                        |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                                       |
| pyflate                 | 676 ms                                                 | 392 ms: 1.72x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 64.1 ms: 1.69x faster                                                       |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                        |
| python_startup          | 14.1 ms                                                | 8.49 ms: 1.66x faster                                                       |
| raytrace                | 467 ms                                                 | 287 ms: 1.63x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 287 us: 1.58x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 74.4 ms: 1.57x faster                                                       |
| chaos                   | 106 ms                                                 | 67.4 ms: 1.57x faster                                                       |
| mako                    | 14.7 ms                                                | 9.38 ms: 1.56x faster                                                       |
| hexiom                  | 9.43 ms                                                | 6.10 ms: 1.55x faster                                                       |
| spectral_norm           | 150 ms                                                 | 97.1 ms: 1.54x faster                                                       |
| unpickle_pure_python    | 302 us                                                 | 197 us: 1.53x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 33.9 us: 1.52x faster                                                       |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| nbody                   | 144 ms                                                 | 95.7 ms: 1.50x faster                                                       |
| float                   | 109 ms                                                 | 73.0 ms: 1.49x faster                                                       |
| chameleon               | 9.17 ms                                                | 6.15 ms: 1.49x faster                                                       |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.28 ms: 1.45x faster                                                       |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 41.2 ns: 1.44x faster                                                       |
| html5lib                | 85.9 ms                                                | 60.0 ms: 1.43x faster                                                       |
| sqlglot_transpile       | 2.43 ms                                                | 1.70 ms: 1.43x faster                                                       |
| pprint_safe_repr        | 953 ms                                                 | 671 ms: 1.42x faster                                                        |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                                       |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.40x faster                                                       |
| logging_format          | 8.85 us                                                | 6.42 us: 1.38x faster                                                       |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                                        |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 46.9 ms: 1.36x faster                                                       |
| async_tree_none         | 711 ms                                                 | 528 ms: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                      |
| scimark_fft             | 421 ms                                                 | 318 ms: 1.33x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                      |
| deepcopy                | 438 us                                                 | 330 us: 1.33x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 647 ms: 1.32x faster                                                        |
| 2to3                    | 335 ms                                                 | 254 ms: 1.32x faster                                                        |
| fannkuch                | 488 ms                                                 | 377 ms: 1.29x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.93 us: 1.29x faster                                                       |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                                        |
| nqueens                 | 100 ms                                                 | 77.8 ms: 1.29x faster                                                       |
| sqlglot_optimize        | 65.2 ms                                                | 50.9 ms: 1.28x faster                                                       |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                        |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.36 ms: 1.25x faster                                                       |
| coroutines              | 31.6 ms                                                | 25.4 ms: 1.25x faster                                                       |
| xml_etree_generate      | 93.8 ms                                                | 76.5 ms: 1.23x faster                                                       |
| bench_thread_pool       | 946 us                                                 | 779 us: 1.21x faster                                                        |
| async_generators        | 426 ms                                                 | 352 ms: 1.21x faster                                                        |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                                       |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.19x faster                                                       |
| sympy_expand            | 534 ms                                                 | 457 ms: 1.17x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.04 us: 1.17x faster                                                       |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                       |
| sympy_str               | 325 ms                                                 | 282 ms: 1.15x faster                                                        |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.60 us: 1.13x faster                                                       |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                                        |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                       |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                        |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| unpickle                | 14.2 us                                                | 12.9 us: 1.10x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                        |
| telco                   | 6.73 ms                                                | 6.30 ms: 1.07x faster                                                       |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.72 sec: 1.01x faster                                                      |
| generators              | 76.4 ms                                                | 76.8 ms: 1.00x slower                                                       |
| unpickle_list           | 4.92 us                                                | 4.96 us: 1.01x slower                                                       |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.08 ms: 1.05x slower                                                       |
| pickle_dict             | 27.6 us                                                | 31.0 us: 1.12x slower                                                       |
| regex_effbot            | 3.19 ms                                                | 3.61 ms: 1.13x slower                                                       |
| coverage                | 74.7 ms                                                | 98.8 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230105-3.12.0a3+-94fa28c/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c.json: mypy
