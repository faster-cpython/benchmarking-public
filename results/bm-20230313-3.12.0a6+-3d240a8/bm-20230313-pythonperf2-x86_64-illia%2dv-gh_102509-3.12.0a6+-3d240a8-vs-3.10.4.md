
# Results vs. 3.10.4

- fork: illia-v
- ref: gh_102509
- machine: linux-x86_64
- commit hash: 3d240a8
- commit date: 2023-03-13
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.23x faster                                                 |
| chameleon      | 9.72 ms                                                      | 7.28 ms: 1.34x faster                                                |
| docutils       | 3.40 sec                                                     | 2.81 sec: 1.21x faster                                               |
| html5lib       | 94.6 ms                                                      | 68.5 ms: 1.38x faster                                                |
| tornado_http   | 152 ms                                                       | 117 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                        | 1.29x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 83.3 ms: 1.65x faster                                                |
| float          | 110 ms                                                       | 72.3 ms: 1.53x faster                                                |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                        | 1.40x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 149 ms: 1.30x faster                                                 |
| regex_v8       | 26.6 ms                                                      | 24.1 ms: 1.10x faster                                                |
| regex_dna      | 259 ms                                                       | 239 ms: 1.08x faster                                                 |
| regex_effbot   | 2.99 ms                                                      | 3.53 ms: 1.18x slower                                                |
| Geometric mean | (ref)                                                        | 1.07x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 206 us: 1.56x faster                                                 |
| pickle_pure_python   | 457 us                                                       | 307 us: 1.49x faster                                                 |
| tomli_loads          | 2.97 sec                                                     | 2.11 sec: 1.41x faster                                               |
| json_dumps           | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                |
| xml_etree_process    | 76.0 ms                                                      | 57.8 ms: 1.31x faster                                                |
| json_loads           | 30.0 us                                                      | 24.2 us: 1.24x faster                                                |
| xml_etree_parse      | 162 ms                                                       | 144 ms: 1.12x faster                                                 |
| xml_etree_generate   | 94.6 ms                                                      | 85.1 ms: 1.11x faster                                                |
| pickle_list          | 4.11 us                                                      | 3.77 us: 1.09x faster                                                |
| unpickle             | 14.2 us                                                      | 13.2 us: 1.07x faster                                                |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                 |
| unpickle_list        | 4.49 us                                                      | 4.44 us: 1.01x faster                                                |
| pickle               | 9.94 us                                                      | 10.2 us: 1.02x slower                                                |
| pickle_dict          | 30.0 us                                                      | 32.3 us: 1.08x slower                                                |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                |
| python_startup_no_site | 7.32 ms                                                      | 8.36 ms: 1.14x slower                                                |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.99 ms: 1.47x faster                                                |
| django_template | 51.5 ms                                                      | 39.6 ms: 1.30x faster                                                |
| genshi_text     | 31.5 ms                                                      | 26.2 ms: 1.20x faster                                                |
| genshi_xml      | 64.7 ms                                                      | 55.1 ms: 1.18x faster                                                |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230313-pythonperf2-x86_64-illia%2dv-gh_102509-3.12.0a6+-3d240a8 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| deltablue                | 7.47 ms                                                      | 3.32 ms: 2.25x faster                                                |
| asyncio_tcp              | 782 ms                                                       | 386 ms: 2.03x faster                                                 |
| asyncio_tcp_ssl          | 3.09 sec                                                     | 1.58 sec: 1.95x faster                                               |
| raytrace                 | 488 ms                                                       | 288 ms: 1.70x faster                                                 |
| logging_silent           | 166 ns                                                       | 99.6 ns: 1.66x faster                                                |
| scimark_monte_carlo      | 109 ms                                                       | 66.4 ms: 1.65x faster                                                |
| nbody                    | 137 ms                                                       | 83.3 ms: 1.65x faster                                                |
| pyflate                  | 697 ms                                                       | 424 ms: 1.64x faster                                                 |
| richards                 | 74.1 ms                                                      | 45.3 ms: 1.63x faster                                                |
| scimark_lu               | 164 ms                                                       | 100 ms: 1.63x faster                                                 |
| go                       | 259 ms                                                       | 159 ms: 1.62x faster                                                 |
| scimark_sor              | 177 ms                                                       | 110 ms: 1.62x faster                                                 |
| generators               | 58.0 ms                                                      | 37.2 ms: 1.56x faster                                                |
| unpickle_pure_python     | 321 us                                                       | 206 us: 1.56x faster                                                 |
| richards_super           | 90.8 ms                                                      | 59.5 ms: 1.53x faster                                                |
| float                    | 110 ms                                                       | 72.3 ms: 1.53x faster                                                |
| spectral_norm            | 136 ms                                                       | 89.5 ms: 1.52x faster                                                |
| bench_mp_pool            | 7.18 ms                                                      | 4.77 ms: 1.50x faster                                                |
| hexiom                   | 9.52 ms                                                      | 6.36 ms: 1.50x faster                                                |
| pickle_pure_python       | 457 us                                                       | 307 us: 1.49x faster                                                 |
| mako                     | 14.7 ms                                                      | 9.99 ms: 1.47x faster                                                |
| sqlglot_parse            | 2.26 ms                                                      | 1.57 ms: 1.44x faster                                                |
| crypto_pyaes             | 118 ms                                                       | 82.8 ms: 1.43x faster                                                |
| tomli_loads              | 2.97 sec                                                     | 2.11 sec: 1.41x faster                                               |
| chaos                    | 107 ms                                                       | 76.1 ms: 1.41x faster                                                |
| sqlglot_transpile        | 2.71 ms                                                      | 1.93 ms: 1.40x faster                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.56 sec: 1.39x faster                                               |
| html5lib                 | 94.6 ms                                                      | 68.5 ms: 1.38x faster                                                |
| scimark_fft              | 359 ms                                                       | 261 ms: 1.38x faster                                                 |
| async_tree_io            | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                               |
| scimark_sparse_mat_mult  | 5.19 ms                                                      | 3.79 ms: 1.37x faster                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 768 ms: 1.37x faster                                                 |
| json_dumps               | 14.2 ms                                                      | 10.4 ms: 1.37x faster                                                |
| async_tree_none          | 700 ms                                                       | 512 ms: 1.37x faster                                                 |
| deepcopy_memo            | 48.9 us                                                      | 36.0 us: 1.36x faster                                                |
| async_tree_memoization   | 824 ms                                                       | 616 ms: 1.34x faster                                                 |
| chameleon                | 9.72 ms                                                      | 7.28 ms: 1.34x faster                                                |
| unpack_sequence          | 59.5 ns                                                      | 45.0 ns: 1.32x faster                                                |
| pycparser                | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                               |
| xml_etree_process        | 76.0 ms                                                      | 57.8 ms: 1.31x faster                                                |
| logging_simple           | 8.90 us                                                      | 6.80 us: 1.31x faster                                                |
| regex_compile            | 194 ms                                                       | 149 ms: 1.30x faster                                                 |
| django_template          | 51.5 ms                                                      | 39.6 ms: 1.30x faster                                                |
| tornado_http             | 152 ms                                                       | 117 ms: 1.30x faster                                                 |
| async_tree_cpu_io_mixed  | 952 ms                                                       | 751 ms: 1.27x faster                                                 |
| logging_format           | 9.57 us                                                      | 7.65 us: 1.25x faster                                                |
| dulwich_log              | 80.1 ms                                                      | 64.3 ms: 1.24x faster                                                |
| json_loads               | 30.0 us                                                      | 24.2 us: 1.24x faster                                                |
| 2to3                     | 350 ms                                                       | 283 ms: 1.23x faster                                                 |
| docutils                 | 3.40 sec                                                     | 2.81 sec: 1.21x faster                                               |
| thrift                   | 1.16 ms                                                      | 960 us: 1.21x faster                                                 |
| fannkuch                 | 496 ms                                                       | 409 ms: 1.21x faster                                                 |
| deepcopy_reduce          | 4.03 us                                                      | 3.34 us: 1.21x faster                                                |
| sqlglot_optimize         | 70.3 ms                                                      | 58.4 ms: 1.20x faster                                                |
| genshi_text              | 31.5 ms                                                      | 26.2 ms: 1.20x faster                                                |
| coroutines               | 30.4 ms                                                      | 25.3 ms: 1.20x faster                                                |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                 |
| pathlib                  | 21.7 ms                                                      | 18.4 ms: 1.18x faster                                                |
| json                     | 5.96 ms                                                      | 5.07 ms: 1.18x faster                                                |
| genshi_xml               | 64.7 ms                                                      | 55.1 ms: 1.18x faster                                                |
| deepcopy                 | 454 us                                                       | 387 us: 1.17x faster                                                 |
| bench_thread_pool        | 1.14 ms                                                      | 971 us: 1.17x faster                                                 |
| mdp                      | 3.03 sec                                                     | 2.62 sec: 1.16x faster                                               |
| sqlite_synth             | 2.97 us                                                      | 2.59 us: 1.15x faster                                                |
| nqueens                  | 112 ms                                                       | 99.9 ms: 1.13x faster                                                |
| xml_etree_parse          | 162 ms                                                       | 144 ms: 1.12x faster                                                 |
| xml_etree_generate       | 94.6 ms                                                      | 85.1 ms: 1.11x faster                                                |
| sympy_expand             | 599 ms                                                       | 540 ms: 1.11x faster                                                 |
| sympy_integrate          | 28.1 ms                                                      | 25.3 ms: 1.11x faster                                                |
| async_generators         | 422 ms                                                       | 382 ms: 1.11x faster                                                 |
| create_gc_cycles         | 1.82 ms                                                      | 1.65 ms: 1.10x faster                                                |
| regex_v8                 | 26.6 ms                                                      | 24.1 ms: 1.10x faster                                                |
| pickle_list              | 4.11 us                                                      | 3.77 us: 1.09x faster                                                |
| regex_dna                | 259 ms                                                       | 239 ms: 1.08x faster                                                 |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                 |
| unpickle                 | 14.2 us                                                      | 13.2 us: 1.07x faster                                                |
| sympy_str                | 358 ms                                                       | 334 ms: 1.07x faster                                                 |
| meteor_contest           | 137 ms                                                       | 129 ms: 1.06x faster                                                 |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                 |
| telco                    | 7.14 ms                                                      | 6.92 ms: 1.03x faster                                                |
| sympy_sum                | 193 ms                                                       | 187 ms: 1.03x faster                                                 |
| typing_runtime_protocols | 523 us                                                       | 513 us: 1.02x faster                                                 |
| python_startup           | 11.5 ms                                                      | 11.3 ms: 1.01x faster                                                |
| unpickle_list            | 4.49 us                                                      | 4.44 us: 1.01x faster                                                |
| pickle                   | 9.94 us                                                      | 10.2 us: 1.02x slower                                                |
| pickle_dict              | 30.0 us                                                      | 32.3 us: 1.08x slower                                                |
| python_startup_no_site   | 7.32 ms                                                      | 8.36 ms: 1.14x slower                                                |
| gc_traversal             | 3.45 ms                                                      | 3.96 ms: 1.15x slower                                                |
| regex_effbot             | 2.99 ms                                                      | 3.53 ms: 1.18x slower                                                |
| dask                     | 463 ms                                                       | 566 ms: 1.22x slower                                                 |
| coverage                 | 64.0 ms                                                      | 80.1 ms: 1.25x slower                                                |
| Geometric mean           | (ref)                                                        | 1.27x faster                                                         |

Benchmark hidden because not significant (1): comprehensions
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
