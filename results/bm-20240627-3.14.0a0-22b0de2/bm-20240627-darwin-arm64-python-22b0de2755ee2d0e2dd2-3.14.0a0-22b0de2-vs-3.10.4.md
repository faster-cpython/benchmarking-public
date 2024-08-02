# Results vs. 3.10.4

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: darwin-arm64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 188 ms: 1.02x faster                                                  |
| docutils       | 1.73 sec                                               | 1.49 sec: 1.17x faster                                                |
| html5lib       | 42.4 ms                                                | 31.8 ms: 1.33x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.2 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 233 ms: 2.03x faster                                                  |
| async_tree_none         | 388 ms                                                 | 194 ms: 2.00x faster                                                  |
| async_tree_io           | 980 ms                                                 | 539 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 452 ms: 1.44x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.0 ms: 1.55x faster                                                 |
| float          | 69.0 ms                                                | 50.6 ms: 1.36x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 69.4 ms: 1.37x faster                                                 |
| regex_dna      | 174 ms                                                 | 150 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.54 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 185 us: 1.52x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 146 us: 1.33x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.46 ms: 1.25x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 38.2 ms: 1.22x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 54.0 ms: 1.01x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.0 ms: 1.01x slower                                                 |
| json_loads           | 16.4 us                                                | 17.6 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.91 ms                                                | 15.6 ms: 1.98x slower                                                 |
| python_startup         | 10.9 ms                                                | 21.5 ms: 1.98x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.98x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.12 ms: 1.39x faster                                                 |
| django_template | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.24x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 29.8 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.7 us: 3.49x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.30x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 17.1 us: 2.04x faster                                                 |
| raytrace                 | 301 ms                                                 | 148 ms: 2.03x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 233 ms: 2.03x faster                                                  |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.00x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.0 ns: 1.92x faster                                                 |
| chaos                    | 65.8 ms                                                | 35.3 ms: 1.87x faster                                                 |
| deepcopy                 | 272 us                                                 | 147 us: 1.84x faster                                                  |
| async_tree_io            | 980 ms                                                 | 539 ms: 1.82x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.0 ms: 1.65x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 763 us: 1.63x faster                                                  |
| pylint                   | 277 ms                                                 | 175 ms: 1.58x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.8 us: 1.57x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 929 us: 1.55x faster                                                  |
| nbody                    | 93.0 ms                                                | 60.0 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                 |
| richards                 | 48.7 ms                                                | 31.8 ms: 1.53x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 185 us: 1.52x faster                                                  |
| go                       | 151 ms                                                 | 100 ms: 1.50x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.13 ms: 1.50x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 441 ms: 1.50x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.0 ms: 1.49x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.08 us: 1.44x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 452 ms: 1.44x faster                                                  |
| generators               | 32.3 ms                                                | 22.7 ms: 1.43x faster                                                 |
| logging_format           | 4.83 us                                                | 3.39 us: 1.42x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.5 ms: 1.42x faster                                                 |
| scimark_lu               | 103 ms                                                 | 72.4 ms: 1.42x faster                                                 |
| mako                     | 9.87 ms                                                | 7.12 ms: 1.39x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.4 ms: 1.39x faster                                                 |
| regex_compile            | 95.3 ms                                                | 69.4 ms: 1.37x faster                                                 |
| float                    | 69.0 ms                                                | 50.6 ms: 1.36x faster                                                 |
| pycparser                | 877 ms                                                 | 643 ms: 1.36x faster                                                  |
| scimark_sor              | 128 ms                                                 | 95.8 ms: 1.34x faster                                                 |
| html5lib                 | 42.4 ms                                                | 31.8 ms: 1.33x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 981 ms: 1.33x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 146 us: 1.33x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 483 ms: 1.33x faster                                                  |
| pyflate                  | 427 ms                                                 | 323 ms: 1.32x faster                                                  |
| django_template          | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                 |
| thrift                   | 572 us                                                 | 436 us: 1.31x faster                                                  |
| tornado_http             | 86.7 ms                                                | 67.2 ms: 1.29x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 71.7 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.46 ms: 1.25x faster                                                 |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.24x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.6 ms: 1.24x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| sympy_str                | 165 ms                                                 | 136 ms: 1.22x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 38.2 ms: 1.22x faster                                                 |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.90 ms: 1.18x faster                                                 |
| nqueens                  | 63.8 ms                                                | 54.0 ms: 1.18x faster                                                 |
| regex_dna                | 174 ms                                                 | 150 ms: 1.17x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.49 sec: 1.17x faster                                                |
| bench_thread_pool        | 527 us                                                 | 455 us: 1.16x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.8 ms: 1.15x faster                                                 |
| sympy_expand             | 269 ms                                                 | 233 ms: 1.15x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.14x faster                                                |
| genshi_xml               | 33.8 ms                                                | 29.8 ms: 1.13x faster                                                 |
| fannkuch                 | 303 ms                                                 | 268 ms: 1.13x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 171 ms: 1.11x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.2 ms: 1.08x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.4 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 3.01 ms: 1.02x faster                                                 |
| 2to3                     | 192 ms                                                 | 188 ms: 1.02x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| xml_etree_generate       | 53.5 ms                                                | 54.0 ms: 1.01x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 73.0 ms: 1.01x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 887 us: 1.03x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.54 ms: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.6 us: 1.07x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.5 ms: 1.10x slower                                                 |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                                  |
| telco                    | 3.49 ms                                                | 4.65 ms: 1.33x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 57.2 ms: 1.53x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 15.6 ms: 1.98x slower                                                 |
| python_startup           | 10.9 ms                                                | 21.5 ms: 1.98x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240627-3.14.0a0-22b0de2/bm-20240627-darwin-arm64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.18x