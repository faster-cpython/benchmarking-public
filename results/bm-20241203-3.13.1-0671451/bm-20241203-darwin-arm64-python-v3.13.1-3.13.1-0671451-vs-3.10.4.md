# Results vs. 3.10.4

- fork: python
- ref: v3.13.1
- machine: darwin-arm64
- commit hash: 0671451
- commit date: 2024-12-03
- overall geometric mean: 1.158x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 181 ms: 1.06x faster                                   |
| chameleon      | 6.26 ms                                                | 5.06 ms: 1.24x faster                                  |
| docutils       | 1.73 sec                                               | 1.43 sec: 1.21x faster                                 |
| html5lib       | 42.4 ms                                                | 36.0 ms: 1.18x faster                                  |
| tornado_http   | 86.7 ms                                                | 71.4 ms: 1.21x faster                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 514 ms: 1.91x faster                                   |
| async_tree_none         | 388 ms                                                 | 213 ms: 1.82x faster                                   |
| async_tree_memoization  | 474 ms                                                 | 271 ms: 1.75x faster                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 461 ms: 1.41x faster                                   |
| Geometric mean          | (ref)                                                  | 1.71x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 73.3 ms: 1.27x faster                                  |
| float          | 69.0 ms                                                | 56.0 ms: 1.23x faster                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 141 ms: 1.24x faster                                   |
| regex_compile  | 95.3 ms                                                | 80.8 ms: 1.18x faster                                  |
| regex_effbot   | 2.46 ms                                                | 2.25 ms: 1.09x faster                                  |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 221 us: 1.27x faster                                   |
| json_dumps           | 8.11 ms                                                | 6.55 ms: 1.24x faster                                  |
| unpickle_pure_python | 194 us                                                 | 165 us: 1.18x faster                                   |
| xml_etree_process    | 46.5 ms                                                | 41.0 ms: 1.13x faster                                  |
| tomli_loads          | 1.71 sec                                               | 1.57 sec: 1.09x faster                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 74.0 ms: 1.03x slower                                  |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                  |
| xml_etree_generate   | 53.5 ms                                                | 56.7 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 20.5 ms: 1.89x slower                                  |
| python_startup_no_site | 7.91 ms                                                | 15.6 ms: 1.98x slower                                  |
| Geometric mean         | (ref)                                                  | 1.93x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.67 ms: 1.29x faster                                  |
| django_template | 26.4 ms                                                | 21.0 ms: 1.26x faster                                  |
| genshi_text     | 17.3 ms                                                | 17.0 ms: 1.02x faster                                  |
| genshi_xml      | 33.8 ms                                                | 34.4 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 100 us: 3.22x faster                                   |
| async_tree_io            | 980 ms                                                 | 514 ms: 1.91x faster                                   |
| deltablue                | 4.91 ms                                                | 2.66 ms: 1.85x faster                                  |
| async_tree_none          | 388 ms                                                 | 213 ms: 1.82x faster                                   |
| async_tree_memoization   | 474 ms                                                 | 271 ms: 1.75x faster                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.69x faster                                   |
| logging_silent           | 117 ns                                                 | 70.5 ns: 1.66x faster                                  |
| raytrace                 | 301 ms                                                 | 182 ms: 1.66x faster                                   |
| chaos                    | 65.8 ms                                                | 41.7 ms: 1.58x faster                                  |
| pylint                   | 277 ms                                                 | 179 ms: 1.54x faster                                   |
| richards_super           | 57.8 ms                                                | 39.7 ms: 1.46x faster                                  |
| sqlglot_parse            | 1.24 ms                                                | 855 us: 1.45x faster                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 461 ms: 1.41x faster                                   |
| sqlglot_transpile        | 1.44 ms                                                | 1.03 ms: 1.40x faster                                  |
| richards                 | 48.7 ms                                                | 35.3 ms: 1.38x faster                                  |
| comprehensions           | 16.9 us                                                | 12.4 us: 1.37x faster                                  |
| scimark_lu               | 103 ms                                                 | 75.9 ms: 1.35x faster                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.69 ms: 1.32x faster                                  |
| crypto_pyaes             | 71.8 ms                                                | 54.6 ms: 1.32x faster                                  |
| go                       | 151 ms                                                 | 115 ms: 1.31x faster                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 50.2 ms: 1.31x faster                                  |
| mako                     | 9.87 ms                                                | 7.67 ms: 1.29x faster                                  |
| pickle_pure_python       | 281 us                                                 | 221 us: 1.27x faster                                   |
| nbody                    | 93.0 ms                                                | 73.3 ms: 1.27x faster                                  |
| deepcopy_memo            | 34.7 us                                                | 27.5 us: 1.26x faster                                  |
| django_template          | 26.4 ms                                                | 21.0 ms: 1.26x faster                                  |
| hexiom                   | 6.19 ms                                                | 4.92 ms: 1.26x faster                                  |
| logging_format           | 4.83 us                                                | 3.86 us: 1.25x faster                                  |
| logging_simple           | 4.45 us                                                | 3.56 us: 1.25x faster                                  |
| pycparser                | 877 ms                                                 | 701 ms: 1.25x faster                                   |
| sqlalchemy_declarative   | 73.3 ms                                                | 59.0 ms: 1.24x faster                                  |
| dulwich_log              | 35.3 ms                                                | 28.5 ms: 1.24x faster                                  |
| chameleon                | 6.26 ms                                                | 5.06 ms: 1.24x faster                                  |
| json_dumps               | 8.11 ms                                                | 6.55 ms: 1.24x faster                                  |
| regex_dna                | 174 ms                                                 | 141 ms: 1.24x faster                                   |
| float                    | 69.0 ms                                                | 56.0 ms: 1.23x faster                                  |
| thrift                   | 572 us                                                 | 466 us: 1.23x faster                                   |
| tornado_http             | 86.7 ms                                                | 71.4 ms: 1.21x faster                                  |
| pyflate                  | 427 ms                                                 | 351 ms: 1.21x faster                                   |
| sympy_sum                | 92.2 ms                                                | 75.9 ms: 1.21x faster                                  |
| docutils                 | 1.73 sec                                               | 1.43 sec: 1.21x faster                                 |
| scimark_sor              | 128 ms                                                 | 106 ms: 1.21x faster                                   |
| pprint_pformat           | 1.30 sec                                               | 1.09 sec: 1.20x faster                                 |
| pprint_safe_repr         | 641 ms                                                 | 535 ms: 1.20x faster                                   |
| spectral_norm            | 94.8 ms                                                | 79.9 ms: 1.19x faster                                  |
| unpickle_pure_python     | 194 us                                                 | 165 us: 1.18x faster                                   |
| regex_compile            | 95.3 ms                                                | 80.8 ms: 1.18x faster                                  |
| html5lib                 | 42.4 ms                                                | 36.0 ms: 1.18x faster                                  |
| deepcopy                 | 272 us                                                 | 234 us: 1.16x faster                                   |
| sympy_integrate          | 13.1 ms                                                | 11.4 ms: 1.16x faster                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.01 ms: 1.14x faster                                  |
| xml_etree_process        | 46.5 ms                                                | 41.0 ms: 1.13x faster                                  |
| sympy_str                | 165 ms                                                 | 146 ms: 1.13x faster                                   |
| deepcopy_reduce          | 2.33 us                                                | 2.07 us: 1.13x faster                                  |
| scimark_fft              | 224 ms                                                 | 200 ms: 1.12x faster                                   |
| gunicorn                 | 1.30 ms                                                | 1.19 ms: 1.10x faster                                  |
| regex_effbot             | 2.46 ms                                                | 2.25 ms: 1.09x faster                                  |
| tomli_loads              | 1.71 sec                                               | 1.57 sec: 1.09x faster                                 |
| fannkuch                 | 303 ms                                                 | 280 ms: 1.08x faster                                   |
| sympy_expand             | 269 ms                                                 | 249 ms: 1.08x faster                                   |
| mdp                      | 1.63 sec                                               | 1.51 sec: 1.08x faster                                 |
| 2to3                     | 192 ms                                                 | 181 ms: 1.06x faster                                   |
| pathlib                  | 24.5 ms                                                | 23.4 ms: 1.05x faster                                  |
| sqlglot_optimize         | 36.8 ms                                                | 35.2 ms: 1.04x faster                                  |
| meteor_contest           | 77.7 ms                                                | 74.5 ms: 1.04x faster                                  |
| coroutines               | 20.7 ms                                                | 19.9 ms: 1.04x faster                                  |
| bench_thread_pool        | 527 us                                                 | 508 us: 1.04x faster                                   |
| generators               | 32.3 ms                                                | 31.4 ms: 1.03x faster                                  |
| genshi_text              | 17.3 ms                                                | 17.0 ms: 1.02x faster                                  |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.02x faster                                  |
| nqueens                  | 63.8 ms                                                | 63.2 ms: 1.01x faster                                  |
| pidigits                 | 282 ms                                                 | 284 ms: 1.00x slower                                   |
| genshi_xml               | 33.8 ms                                                | 34.4 ms: 1.02x slower                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.0 ms: 1.03x slower                                  |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                  |
| xml_etree_generate       | 53.5 ms                                                | 56.7 ms: 1.06x slower                                  |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                  |
| flaskblogging            | 2.65 ms                                                | 2.84 ms: 1.07x slower                                  |
| coverage                 | 41.5 ms                                                | 45.8 ms: 1.10x slower                                  |
| gc_traversal             | 2.36 ms                                                | 2.92 ms: 1.23x slower                                  |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                   |
| telco                    | 3.49 ms                                                | 4.77 ms: 1.37x slower                                  |
| create_gc_cycles         | 860 us                                                 | 1.18 ms: 1.37x slower                                  |
| bench_mp_pool            | 37.4 ms                                                | 64.7 ms: 1.73x slower                                  |
| python_startup           | 10.9 ms                                                | 20.5 ms: 1.89x slower                                  |
| python_startup_no_site   | 7.91 ms                                                | 15.6 ms: 1.98x slower                                  |
| dask                     | 253 ms                                                 | 771 ms: 3.05x slower                                   |
| Geometric mean           | (ref)                                                  | 1.15x faster                                           |

Benchmark hidden because not significant (3): xml_etree_parse, json, sqlglot_normalize
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (21) of results/bm-20241203-3.13.1-0671451/bm-20241203-darwin-arm64-python-v3.13.1-3.13.1-0671451.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.158x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.30x