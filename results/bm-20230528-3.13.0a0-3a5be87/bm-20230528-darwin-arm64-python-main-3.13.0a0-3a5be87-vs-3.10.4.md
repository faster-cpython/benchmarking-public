
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3a5be87
- commit date: 2023-05-28
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.57 sec: 1.14x faster                                |
| html5lib       | 44.1 ms                                                | 37.4 ms: 1.18x faster                                 |
| tornado_http   | 91.9 ms                                                | 71.8 ms: 1.28x faster                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 67.7 ms: 1.39x faster                                 |
| float          | 72.3 ms                                                | 58.9 ms: 1.23x faster                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 79.1 ms: 1.22x faster                                 |
| regex_v8       | 17.5 ms                                                | 16.2 ms: 1.08x faster                                 |
| regex_dna      | 160 ms                                                 | 151 ms: 1.06x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.71 ms: 1.11x slower                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 195 us: 1.45x faster                                  |
| unpickle_pure_python | 203 us                                                 | 153 us: 1.33x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.91 ms: 1.21x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.49 sec: 1.18x faster                                |
| xml_etree_process    | 45.1 ms                                                | 40.5 ms: 1.11x faster                                 |
| xml_etree_parse      | 107 ms                                                 | 108 ms: 1.01x slower                                  |
| unpickle             | 9.77 us                                                | 9.94 us: 1.02x slower                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 75.5 ms: 1.04x slower                                 |
| pickle_dict          | 17.8 us                                                | 18.8 us: 1.06x slower                                 |
| json_loads           | 16.9 us                                                | 17.9 us: 1.06x slower                                 |
| pickle_list          | 2.83 us                                                | 3.01 us: 1.06x slower                                 |
| pickle               | 7.36 us                                                | 7.86 us: 1.07x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 58.1 ms: 1.07x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.16 us: 1.19x slower                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.1 ms: 1.13x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 9.16 ms: 1.06x faster                                 |
| Geometric mean         | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako           | 10.5 ms                                                | 7.69 ms: 1.36x faster                                 |
| genshi_text    | 18.4 ms                                                | 15.3 ms: 1.20x faster                                 |
| genshi_xml     | 37.6 ms                                                | 31.4 ms: 1.20x faster                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230528-darwin-arm64-python-main-3.13.0a0-3a5be87 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 91.7 us: 3.75x faster                                 |
| deltablue                | 5.15 ms                                                | 2.49 ms: 2.07x faster                                 |
| logging_silent           | 119 ns                                                 | 70.7 ns: 1.69x faster                                 |
| richards_super           | 60.7 ms                                                | 37.3 ms: 1.63x faster                                 |
| richards                 | 51.4 ms                                                | 33.2 ms: 1.55x faster                                 |
| async_tree_memoization   | 493 ms                                                 | 331 ms: 1.49x faster                                  |
| scimark_sor              | 127 ms                                                 | 85.0 ms: 1.49x faster                                 |
| go                       | 165 ms                                                 | 111 ms: 1.49x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 910 us: 1.46x faster                                  |
| asyncio_tcp              | 673 ms                                                 | 462 ms: 1.46x faster                                  |
| hexiom                   | 6.32 ms                                                | 4.35 ms: 1.45x faster                                 |
| pickle_pure_python       | 284 us                                                 | 195 us: 1.45x faster                                  |
| async_tree_io            | 1.02 sec                                               | 712 ms: 1.43x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 54.9 ms: 1.42x faster                                 |
| async_tree_none          | 402 ms                                                 | 283 ms: 1.42x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.09 ms: 1.41x faster                                 |
| chaos                    | 66.8 ms                                                | 47.4 ms: 1.41x faster                                 |
| nbody                    | 94.1 ms                                                | 67.7 ms: 1.39x faster                                 |
| scimark_lu               | 110 ms                                                 | 79.2 ms: 1.39x faster                                 |
| scimark_monte_carlo      | 72.2 ms                                                | 52.4 ms: 1.38x faster                                 |
| mako                     | 10.5 ms                                                | 7.69 ms: 1.36x faster                                 |
| unpack_sequence          | 38.7 ns                                                | 28.6 ns: 1.35x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 25.8 us: 1.34x faster                                 |
| unpickle_pure_python     | 203 us                                                 | 153 us: 1.33x faster                                  |
| pyflate                  | 453 ms                                                 | 345 ms: 1.31x faster                                  |
| raytrace                 | 328 ms                                                 | 250 ms: 1.31x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.26 sec: 1.31x faster                                |
| pycparser                | 915 ms                                                 | 701 ms: 1.30x faster                                  |
| tornado_http             | 91.9 ms                                                | 71.8 ms: 1.28x faster                                 |
| generators               | 32.9 ms                                                | 25.9 ms: 1.27x faster                                 |
| create_gc_cycles         | 876 us                                                 | 698 us: 1.26x faster                                  |
| logging_format           | 5.01 us                                                | 4.04 us: 1.24x faster                                 |
| logging_simple           | 4.63 us                                                | 3.75 us: 1.23x faster                                 |
| float                    | 72.3 ms                                                | 58.9 ms: 1.23x faster                                 |
| spectral_norm            | 96.4 ms                                                | 78.7 ms: 1.23x faster                                 |
| regex_compile            | 96.6 ms                                                | 79.1 ms: 1.22x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 549 ms: 1.22x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.91 ms: 1.21x faster                                 |
| genshi_text              | 18.4 ms                                                | 15.3 ms: 1.20x faster                                 |
| dulwich_log              | 37.1 ms                                                | 30.9 ms: 1.20x faster                                 |
| genshi_xml               | 37.6 ms                                                | 31.4 ms: 1.20x faster                                 |
| pprint_pformat           | 1.24 sec                                               | 1.04 sec: 1.19x faster                                |
| pprint_safe_repr         | 609 ms                                                 | 512 ms: 1.19x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.49 sec: 1.18x faster                                |
| html5lib                 | 44.1 ms                                                | 37.4 ms: 1.18x faster                                 |
| deepcopy                 | 278 us                                                 | 237 us: 1.17x faster                                  |
| mypy2                    | 308 ms                                                 | 265 ms: 1.16x faster                                  |
| fannkuch                 | 317 ms                                                 | 276 ms: 1.15x faster                                  |
| docutils                 | 1.78 sec                                               | 1.57 sec: 1.14x faster                                |
| python_startup           | 12.6 ms                                                | 11.1 ms: 1.13x faster                                 |
| scimark_fft              | 232 ms                                                 | 207 ms: 1.12x faster                                  |
| xml_etree_process        | 45.1 ms                                                | 40.5 ms: 1.11x faster                                 |
| deepcopy_reduce          | 2.38 us                                                | 2.15 us: 1.11x faster                                 |
| coroutines               | 20.2 ms                                                | 18.3 ms: 1.11x faster                                 |
| bench_thread_pool        | 548 us                                                 | 502 us: 1.09x faster                                  |
| comprehensions           | 17.7 us                                                | 16.3 us: 1.09x faster                                 |
| regex_v8                 | 17.5 ms                                                | 16.2 ms: 1.08x faster                                 |
| nqueens                  | 68.1 ms                                                | 63.4 ms: 1.07x faster                                 |
| mdp                      | 1.67 sec                                               | 1.56 sec: 1.07x faster                                |
| meteor_contest           | 78.6 ms                                                | 73.8 ms: 1.07x faster                                 |
| python_startup_no_site   | 9.73 ms                                                | 9.16 ms: 1.06x faster                                 |
| regex_dna                | 160 ms                                                 | 151 ms: 1.06x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 36.0 ms: 1.06x faster                                 |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.30 ms: 1.05x faster                                 |
| json                     | 3.10 ms                                                | 3.05 ms: 1.02x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 194 ms: 1.01x faster                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.01x faster                                  |
| xml_etree_parse          | 107 ms                                                 | 108 ms: 1.01x slower                                  |
| gc_traversal             | 2.40 ms                                                | 2.42 ms: 1.01x slower                                 |
| unpickle                 | 9.77 us                                                | 9.94 us: 1.02x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 75.5 ms: 1.04x slower                                 |
| pickle_dict              | 17.8 us                                                | 18.8 us: 1.06x slower                                 |
| json_loads               | 16.9 us                                                | 17.9 us: 1.06x slower                                 |
| pickle_list              | 2.83 us                                                | 3.01 us: 1.06x slower                                 |
| pickle                   | 7.36 us                                                | 7.86 us: 1.07x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 58.1 ms: 1.07x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.59 us: 1.08x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.71 ms: 1.11x slower                                 |
| telco                    | 3.68 ms                                                | 4.10 ms: 1.11x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 45.8 ms: 1.12x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.16 us: 1.19x slower                                 |
| async_generators         | 233 ms                                                 | 324 ms: 1.39x slower                                  |
| coverage                 | 40.8 ms                                                | 57.6 ms: 1.41x slower                                 |
| Geometric mean           | (ref)                                                  | 1.19x faster                                          |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
