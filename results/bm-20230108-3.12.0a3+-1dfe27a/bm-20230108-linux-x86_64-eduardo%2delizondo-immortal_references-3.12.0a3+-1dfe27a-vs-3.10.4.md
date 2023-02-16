
# Results vs. 3.10.4

- fork: eduardo-elizondo
- ref: immortal_references
- machine: linux-x86_64
- commit hash: 1dfe27a
- commit date: 2023-01-08
- overall geometric mean: 1.22x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 274 ms: 1.23x faster                                                              |
| chameleon      | 9.17 ms                                                | 6.83 ms: 1.34x faster                                                             |
| docutils       | 3.18 sec                                               | 2.69 sec: 1.18x faster                                                            |
| html5lib       | 85.9 ms                                                | 64.0 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.7 ms: 1.49x faster                                                             |
| float          | 109 ms                                                 | 79.7 ms: 1.37x faster                                                             |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                             |
| regex_dna      | 214 ms                                                 | 203 ms: 1.05x faster                                                              |
| regex_effbot   | 3.19 ms                                                | 3.39 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 309 us: 1.46x faster                                                              |
| unpickle_pure_python | 302 us                                                 | 217 us: 1.39x faster                                                              |
| json_dumps           | 13.4 ms                                                | 9.78 ms: 1.37x faster                                                             |
| xml_etree_process    | 74.5 ms                                                | 56.7 ms: 1.32x faster                                                             |
| xml_etree_generate   | 93.8 ms                                                | 79.5 ms: 1.18x faster                                                             |
| pickle_list          | 4.72 us                                                | 4.35 us: 1.09x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 151 ms: 1.08x faster                                                              |
| json_loads           | 28.7 us                                                | 26.6 us: 1.08x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                              |
| unpickle             | 14.2 us                                                | 13.7 us: 1.03x faster                                                             |
| unpickle_list        | 4.92 us                                                | 4.79 us: 1.03x faster                                                             |
| pickle               | 10.2 us                                                | 10.5 us: 1.03x slower                                                             |
| pickle_dict          | 27.6 us                                                | 30.5 us: 1.11x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.77 ms: 1.61x faster                                                             |
| python_startup_no_site | 5.78 ms                                                | 6.21 ms: 1.07x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.22x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.5 ms: 1.40x faster                                                             |
| genshi_text     | 30.6 ms                                                | 22.2 ms: 1.38x faster                                                             |
| django_template | 46.3 ms                                                | 34.8 ms: 1.33x faster                                                             |
| genshi_xml      | 63.7 ms                                                | 51.0 ms: 1.25x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.68 ms: 1.98x faster                                                             |
| asyncio_tcp             | 914 ms                                                 | 514 ms: 1.78x faster                                                              |
| logging_silent          | 176 ns                                                 | 101 ns: 1.75x faster                                                              |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                              |
| richards                | 75.2 ms                                                | 44.9 ms: 1.67x faster                                                             |
| scimark_sor             | 197 ms                                                 | 121 ms: 1.63x faster                                                              |
| python_startup          | 14.1 ms                                                | 8.77 ms: 1.61x faster                                                             |
| pyflate                 | 676 ms                                                 | 429 ms: 1.58x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                 | 69.6 ms: 1.56x faster                                                             |
| chaos                   | 106 ms                                                 | 69.2 ms: 1.53x faster                                                             |
| raytrace                | 467 ms                                                 | 309 ms: 1.51x faster                                                              |
| nbody                   | 144 ms                                                 | 96.7 ms: 1.49x faster                                                             |
| hexiom                  | 9.43 ms                                                | 6.38 ms: 1.48x faster                                                             |
| crypto_pyaes            | 117 ms                                                 | 79.0 ms: 1.48x faster                                                             |
| pickle_pure_python      | 452 us                                                 | 309 us: 1.46x faster                                                              |
| spectral_norm           | 150 ms                                                 | 106 ms: 1.41x faster                                                              |
| mako                    | 14.7 ms                                                | 10.5 ms: 1.40x faster                                                             |
| scimark_lu              | 161 ms                                                 | 115 ms: 1.40x faster                                                              |
| unpickle_pure_python    | 302 us                                                 | 217 us: 1.39x faster                                                              |
| genshi_text             | 30.6 ms                                                | 22.2 ms: 1.38x faster                                                             |
| json_dumps              | 13.4 ms                                                | 9.78 ms: 1.37x faster                                                             |
| float                   | 109 ms                                                 | 79.7 ms: 1.37x faster                                                             |
| deepcopy_memo           | 51.7 us                                                | 38.0 us: 1.36x faster                                                             |
| html5lib                | 85.9 ms                                                | 64.0 ms: 1.34x faster                                                             |
| chameleon               | 9.17 ms                                                | 6.83 ms: 1.34x faster                                                             |
| thrift                  | 1.03 ms                                                | 775 us: 1.33x faster                                                              |
| pprint_pformat          | 1.98 sec                                               | 1.49 sec: 1.33x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.34 sec: 1.33x faster                                                            |
| django_template         | 46.3 ms                                                | 34.8 ms: 1.33x faster                                                             |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                            |
| async_tree_none         | 711 ms                                                 | 536 ms: 1.33x faster                                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.55 ms: 1.32x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 56.7 ms: 1.32x faster                                                             |
| pprint_safe_repr        | 953 ms                                                 | 729 ms: 1.31x faster                                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.87 ms: 1.30x faster                                                             |
| logging_simple          | 8.10 us                                                | 6.31 us: 1.28x faster                                                             |
| logging_format          | 8.85 us                                                | 6.96 us: 1.27x faster                                                             |
| fannkuch                | 488 ms                                                 | 387 ms: 1.26x faster                                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.34 ms: 1.26x faster                                                             |
| genshi_xml              | 63.7 ms                                                | 51.0 ms: 1.25x faster                                                             |
| nqueens                 | 100 ms                                                 | 80.1 ms: 1.25x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 688 ms: 1.24x faster                                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 765 ms: 1.24x faster                                                              |
| regex_compile           | 177 ms                                                 | 144 ms: 1.23x faster                                                              |
| 2to3                    | 335 ms                                                 | 274 ms: 1.23x faster                                                              |
| deepcopy                | 438 us                                                 | 366 us: 1.20x faster                                                              |
| coroutines              | 31.6 ms                                                | 26.6 ms: 1.19x faster                                                             |
| regex_v8                | 25.0 ms                                                | 21.1 ms: 1.19x faster                                                             |
| sqlglot_normalize       | 134 ms                                                 | 114 ms: 1.18x faster                                                              |
| sqlglot_optimize        | 65.2 ms                                                | 55.2 ms: 1.18x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 79.5 ms: 1.18x faster                                                             |
| docutils                | 3.18 sec                                               | 2.69 sec: 1.18x faster                                                            |
| deepcopy_reduce         | 3.79 us                                                | 3.21 us: 1.18x faster                                                             |
| scimark_fft             | 421 ms                                                 | 359 ms: 1.17x faster                                                              |
| unpack_sequence         | 59.4 ns                                                | 51.6 ns: 1.15x faster                                                             |
| async_generators        | 426 ms                                                 | 375 ms: 1.14x faster                                                              |
| bench_thread_pool       | 946 us                                                 | 834 us: 1.13x faster                                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                                             |
| sqlite_synth            | 2.92 us                                                | 2.65 us: 1.10x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 68.7 ms: 1.10x faster                                                             |
| djangocms               | 36.9 us                                                | 33.6 us: 1.10x faster                                                             |
| sympy_integrate         | 24.0 ms                                                | 22.0 ms: 1.09x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                             |
| pickle_list             | 4.72 us                                                | 4.35 us: 1.09x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 151 ms: 1.08x faster                                                              |
| json_loads              | 28.7 us                                                | 26.6 us: 1.08x faster                                                             |
| json                    | 5.35 ms                                                | 5.00 ms: 1.07x faster                                                             |
| sympy_expand            | 534 ms                                                 | 501 ms: 1.07x faster                                                              |
| regex_dna               | 214 ms                                                 | 203 ms: 1.05x faster                                                              |
| mdp                     | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                              |
| sympy_str               | 325 ms                                                 | 311 ms: 1.04x faster                                                              |
| unpickle                | 14.2 us                                                | 13.7 us: 1.03x faster                                                             |
| unpickle_list           | 4.92 us                                                | 4.79 us: 1.03x faster                                                             |
| telco                   | 6.73 ms                                                | 6.64 ms: 1.01x faster                                                             |
| sympy_sum               | 183 ms                                                 | 182 ms: 1.01x faster                                                              |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                              |
| meteor_contest          | 114 ms                                                 | 116 ms: 1.02x slower                                                              |
| pickle                  | 10.2 us                                                | 10.5 us: 1.03x slower                                                             |
| generators              | 76.4 ms                                                | 80.5 ms: 1.05x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.39 ms: 1.06x slower                                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.21 ms: 1.07x slower                                                             |
| pickle_dict             | 27.6 us                                                | 30.5 us: 1.11x slower                                                             |
| gc_traversal            | 3.53 ms                                                | 3.90 ms: 1.11x slower                                                             |
| dask                    | 436 ms                                                 | 545 ms: 1.25x slower                                                              |
| coverage                | 74.7 ms                                                | 102 ms: 1.37x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.22x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230108-3.12.0a3+-1dfe27a/bm-20230108-linux-x86_64-eduardo%2delizondo-immortal_references-3.12.0a3+-1dfe27a.json: mypy
