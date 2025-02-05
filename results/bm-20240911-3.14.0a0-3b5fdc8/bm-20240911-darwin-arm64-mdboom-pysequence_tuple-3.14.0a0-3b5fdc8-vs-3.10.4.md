# Results vs. 3.10.4

- fork: mdboom
- ref: pysequence_tuple
- machine: darwin-arm64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.302x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 0.83x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 158 ms: 1.21x faster                                              |
| docutils       | 1.73 sec                                               | 1.43 sec: 1.21x faster                                            |
| html5lib       | 42.4 ms                                                | 30.3 ms: 1.40x faster                                             |
| Geometric mean | (ref)                                                  | 1.22x faster                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 199 ms: 1.95x faster                                              |
| async_tree_memoization  | 474 ms                                                 | 247 ms: 1.92x faster                                              |
| async_tree_io           | 980 ms                                                 | 581 ms: 1.69x faster                                              |
| async_tree_cpu_io_mixed | 649 ms                                                 | 460 ms: 1.41x faster                                              |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.7 ms: 1.53x faster                                             |
| float          | 69.0 ms                                                | 49.2 ms: 1.40x faster                                             |
| Geometric mean | (ref)                                                  | 1.29x faster                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.2 ms: 1.42x faster                                             |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                              |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.15x faster                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                              |
| unpickle_pure_python | 194 us                                                 | 141 us: 1.38x faster                                              |
| json_dumps           | 8.11 ms                                                | 6.41 ms: 1.27x faster                                             |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.24x faster                                             |
| tomli_loads          | 1.71 sec                                               | 1.50 sec: 1.13x faster                                            |
| xml_etree_generate   | 53.5 ms                                                | 53.1 ms: 1.01x faster                                             |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                              |
| xml_etree_iterparse  | 72.1 ms                                                | 73.8 ms: 1.02x slower                                             |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                             |
| unpickle             | 8.80 us                                                | 9.21 us: 1.05x slower                                             |
| pickle               | 6.97 us                                                | 7.38 us: 1.06x slower                                             |
| pickle_list          | 2.74 us                                                | 2.95 us: 1.08x slower                                             |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                             |
| unpickle_list        | 2.69 us                                                | 2.91 us: 1.08x slower                                             |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.0 ms: 1.56x slower                                             |
| python_startup_no_site | 7.91 ms                                                | 13.7 ms: 1.73x slower                                             |
| Geometric mean         | (ref)                                                  | 1.64x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.00 ms: 1.41x faster                                             |
| django_template | 26.4 ms                                                | 19.6 ms: 1.35x faster                                             |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                             |
| genshi_xml      | 33.8 ms                                                | 30.5 ms: 1.11x faster                                             |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.7 us: 3.52x faster                                             |
| deltablue                | 4.91 ms                                                | 2.13 ms: 2.31x faster                                             |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.11x faster                                             |
| raytrace                 | 301 ms                                                 | 148 ms: 2.03x faster                                              |
| async_tree_none          | 388 ms                                                 | 199 ms: 1.95x faster                                              |
| logging_silent           | 117 ns                                                 | 60.5 ns: 1.94x faster                                             |
| async_tree_memoization   | 474 ms                                                 | 247 ms: 1.92x faster                                              |
| go                       | 151 ms                                                 | 79.2 ms: 1.90x faster                                             |
| chaos                    | 65.8 ms                                                | 34.9 ms: 1.89x faster                                             |
| deepcopy                 | 272 us                                                 | 145 us: 1.88x faster                                              |
| richards_super           | 57.8 ms                                                | 33.5 ms: 1.73x faster                                             |
| comprehensions           | 16.9 us                                                | 10.0 us: 1.69x faster                                             |
| async_tree_io            | 980 ms                                                 | 581 ms: 1.69x faster                                              |
| sqlglot_parse            | 1.24 ms                                                | 744 us: 1.67x faster                                              |
| richards                 | 48.7 ms                                                | 30.3 ms: 1.61x faster                                             |
| sqlglot_transpile        | 1.44 ms                                                | 907 us: 1.59x faster                                              |
| generators               | 32.3 ms                                                | 20.4 ms: 1.59x faster                                             |
| asyncio_tcp              | 659 ms                                                 | 419 ms: 1.57x faster                                              |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.55x faster                                             |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                              |
| nbody                    | 93.0 ms                                                | 60.7 ms: 1.53x faster                                             |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                              |
| scimark_lu               | 103 ms                                                 | 67.7 ms: 1.52x faster                                             |
| scimark_monte_carlo      | 65.6 ms                                                | 43.4 ms: 1.51x faster                                             |
| hexiom                   | 6.19 ms                                                | 4.11 ms: 1.51x faster                                             |
| logging_simple           | 4.45 us                                                | 3.01 us: 1.48x faster                                             |
| logging_format           | 4.83 us                                                | 3.32 us: 1.45x faster                                             |
| crypto_pyaes             | 71.8 ms                                                | 50.2 ms: 1.43x faster                                             |
| pprint_safe_repr         | 641 ms                                                 | 448 ms: 1.43x faster                                              |
| unpack_sequence          | 39.0 ns                                                | 27.4 ns: 1.42x faster                                             |
| pprint_pformat           | 1.30 sec                                               | 919 ms: 1.42x faster                                              |
| regex_compile            | 95.3 ms                                                | 67.2 ms: 1.42x faster                                             |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 460 ms: 1.41x faster                                              |
| mako                     | 9.87 ms                                                | 7.00 ms: 1.41x faster                                             |
| spectral_norm            | 94.8 ms                                                | 67.3 ms: 1.41x faster                                             |
| float                    | 69.0 ms                                                | 49.2 ms: 1.40x faster                                             |
| html5lib                 | 42.4 ms                                                | 30.3 ms: 1.40x faster                                             |
| pycparser                | 877 ms                                                 | 636 ms: 1.38x faster                                              |
| unpickle_pure_python     | 194 us                                                 | 141 us: 1.38x faster                                              |
| scimark_sor              | 128 ms                                                 | 93.2 ms: 1.38x faster                                             |
| django_template          | 26.4 ms                                                | 19.6 ms: 1.35x faster                                             |
| thrift                   | 572 us                                                 | 425 us: 1.35x faster                                              |
| sympy_sum                | 92.2 ms                                                | 68.9 ms: 1.34x faster                                             |
| pyflate                  | 427 ms                                                 | 322 ms: 1.33x faster                                              |
| dulwich_log              | 35.3 ms                                                | 27.1 ms: 1.30x faster                                             |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                             |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                             |
| json_dumps               | 8.11 ms                                                | 6.41 ms: 1.27x faster                                             |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                              |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                            |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.24x faster                                             |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                             |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.82 ms: 1.22x faster                                             |
| docutils                 | 1.73 sec                                               | 1.43 sec: 1.21x faster                                            |
| 2to3                     | 192 ms                                                 | 158 ms: 1.21x faster                                              |
| scimark_fft              | 224 ms                                                 | 186 ms: 1.21x faster                                              |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                              |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                             |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                              |
| sqlglot_optimize         | 36.8 ms                                                | 31.2 ms: 1.18x faster                                             |
| bench_thread_pool        | 527 us                                                 | 449 us: 1.18x faster                                              |
| fannkuch                 | 303 ms                                                 | 260 ms: 1.16x faster                                              |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                            |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                              |
| tomli_loads              | 1.71 sec                                               | 1.50 sec: 1.13x faster                                            |
| genshi_xml               | 33.8 ms                                                | 30.5 ms: 1.11x faster                                             |
| meteor_contest           | 77.7 ms                                                | 71.5 ms: 1.09x faster                                             |
| json                     | 3.08 ms                                                | 2.97 ms: 1.04x faster                                             |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                             |
| pathlib                  | 24.5 ms                                                | 23.8 ms: 1.03x faster                                             |
| xml_etree_generate       | 53.5 ms                                                | 53.1 ms: 1.01x faster                                             |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.01x slower                                              |
| xml_etree_iterparse      | 72.1 ms                                                | 73.8 ms: 1.02x slower                                             |
| create_gc_cycles         | 860 us                                                 | 892 us: 1.04x slower                                              |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                             |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                             |
| unpickle                 | 8.80 us                                                | 9.21 us: 1.05x slower                                             |
| pickle                   | 6.97 us                                                | 7.38 us: 1.06x slower                                             |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                             |
| coverage                 | 41.5 ms                                                | 44.4 ms: 1.07x slower                                             |
| pickle_list              | 2.74 us                                                | 2.95 us: 1.08x slower                                             |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                             |
| unpickle_list            | 2.69 us                                                | 2.91 us: 1.08x slower                                             |
| async_generators         | 231 ms                                                 | 279 ms: 1.20x slower                                              |
| bench_mp_pool            | 37.4 ms                                                | 49.2 ms: 1.32x slower                                             |
| telco                    | 3.49 ms                                                | 4.81 ms: 1.38x slower                                             |
| python_startup           | 10.9 ms                                                | 17.0 ms: 1.56x slower                                             |
| python_startup_no_site   | 7.91 ms                                                | 13.7 ms: 1.73x slower                                             |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                      |

Benchmark hidden because not significant (4): tornado_http, asyncio_websockets, regex_effbot, pidigits
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-darwin-arm64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.302x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 0.83x