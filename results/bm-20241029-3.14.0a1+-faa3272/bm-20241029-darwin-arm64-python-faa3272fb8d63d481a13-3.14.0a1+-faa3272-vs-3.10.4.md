# Results vs. 3.10.4

- fork: python
- ref: faa3272fb8d63d481a13
- machine: darwin-arm64
- commit hash: faa3272
- commit date: 2024-10-29
- overall geometric mean: 1.292x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 165 ms: 1.16x faster                                                   |
| docutils       | 1.73 sec                                               | 1.41 sec: 1.23x faster                                                 |
| html5lib       | 42.4 ms                                                | 30.2 ms: 1.40x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 200 ms: 1.94x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 247 ms: 1.91x faster                                                   |
| async_tree_io           | 980 ms                                                 | 596 ms: 1.64x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 65.5 ms: 1.42x faster                                                  |
| float          | 69.0 ms                                                | 49.5 ms: 1.39x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.6 ms: 1.39x faster                                                  |
| regex_dna      | 174 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8       | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.44 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 184 us: 1.52x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.15x faster                                                 |
| json_dumps           | 8.11 ms                                                | 7.26 ms: 1.12x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                | 52.7 ms: 1.02x faster                                                  |
| json_loads           | 16.4 us                                                | 16.5 us: 1.00x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 73.6 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.8 ms: 1.54x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 12.2 ms: 1.54x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.54x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.60 ms: 1.50x faster                                                  |
| django_template | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                  |
| genshi_text     | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 30.0 ms: 1.13x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.4 us: 3.50x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.25 ms: 2.18x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.0 us: 2.04x faster                                                  |
| raytrace                 | 301 ms                                                 | 154 ms: 1.96x faster                                                   |
| async_tree_none          | 388 ms                                                 | 200 ms: 1.94x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 247 ms: 1.91x faster                                                   |
| logging_silent           | 117 ns                                                 | 62.6 ns: 1.87x faster                                                  |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                   |
| go                       | 151 ms                                                 | 82.9 ms: 1.82x faster                                                  |
| chaos                    | 65.8 ms                                                | 36.3 ms: 1.81x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 743 us: 1.67x faster                                                   |
| async_tree_io            | 980 ms                                                 | 596 ms: 1.64x faster                                                   |
| generators               | 32.3 ms                                                | 20.2 ms: 1.60x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 907 us: 1.59x faster                                                   |
| richards                 | 48.7 ms                                                | 31.1 ms: 1.56x faster                                                  |
| pylint                   | 277 ms                                                 | 179 ms: 1.55x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 184 us: 1.52x faster                                                   |
| scimark_lu               | 103 ms                                                 | 67.6 ms: 1.52x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.6 ms: 1.50x faster                                                  |
| mako                     | 9.87 ms                                                | 6.60 ms: 1.50x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.14 ms: 1.50x faster                                                  |
| comprehensions           | 16.9 us                                                | 11.4 us: 1.49x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.06 us: 1.45x faster                                                  |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                  |
| nbody                    | 93.0 ms                                                | 65.5 ms: 1.42x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 51.2 ms: 1.40x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.2 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 458 ms: 1.40x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 935 ms: 1.39x faster                                                   |
| float                    | 69.0 ms                                                | 49.5 ms: 1.39x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.37 ms: 1.39x faster                                                  |
| regex_compile            | 95.3 ms                                                | 68.6 ms: 1.39x faster                                                  |
| pycparser                | 877 ms                                                 | 638 ms: 1.37x faster                                                   |
| thrift                   | 572 us                                                 | 416 us: 1.37x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 69.5 ms: 1.36x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                   |
| django_template          | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                  |
| scimark_sor              | 128 ms                                                 | 96.2 ms: 1.33x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.9 ms: 1.32x faster                                                  |
| pyflate                  | 427 ms                                                 | 325 ms: 1.31x faster                                                   |
| sqlalchemy_declarative   | 73.3 ms                                                | 56.1 ms: 1.30x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.2 ms: 1.30x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                  |
| regex_dna                | 174 ms                                                 | 141 ms: 1.24x faster                                                   |
| sympy_str                | 165 ms                                                 | 135 ms: 1.23x faster                                                   |
| xml_etree_process        | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.41 sec: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.82 ms: 1.21x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 438 us: 1.20x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.19x faster                                                  |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.18x faster                                                   |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 31.4 ms: 1.17x faster                                                  |
| nqueens                  | 63.8 ms                                                | 54.7 ms: 1.17x faster                                                  |
| 2to3                     | 192 ms                                                 | 165 ms: 1.16x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.15x faster                                                 |
| fannkuch                 | 303 ms                                                 | 265 ms: 1.14x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 168 ms: 1.13x faster                                                   |
| genshi_xml               | 33.8 ms                                                | 30.0 ms: 1.13x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.26 ms: 1.12x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.47 sec: 1.11x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.1 ms: 1.09x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.09x faster                                                  |
| json                     | 3.08 ms                                                | 2.89 ms: 1.07x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| xml_etree_generate       | 53.5 ms                                                | 52.7 ms: 1.02x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.44 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| json_loads               | 16.4 us                                                | 16.5 us: 1.00x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.6 ms: 1.02x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.51 us: 1.03x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.0 ms: 1.06x slower                                                  |
| async_generators         | 231 ms                                                 | 277 ms: 1.20x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.97 ms: 1.26x slower                                                  |
| telco                    | 3.49 ms                                                | 4.64 ms: 1.33x slower                                                  |
| python_startup           | 10.9 ms                                                | 16.8 ms: 1.54x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 12.2 ms: 1.54x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.33 ms: 1.55x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 58.5 ms: 1.56x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20241029-3.14.0a1+-faa3272/bm-20241029-darwin-arm64-python-faa3272fb8d63d481a13-3.14.0a1+-faa3272.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.292x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.31x