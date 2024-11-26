# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: darwin-arm64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.181x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.44x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 193 ms: 1.01x slower                                                         |
| docutils       | 1.73 sec                                               | 1.61 sec: 1.08x faster                                                       |
| html5lib       | 42.4 ms                                                | 33.5 ms: 1.27x faster                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 257 ms: 1.84x faster                                                         |
| async_tree_none         | 388 ms                                                 | 212 ms: 1.83x faster                                                         |
| async_tree_io           | 980 ms                                                 | 596 ms: 1.64x faster                                                         |
| async_tree_cpu_io_mixed | 649 ms                                                 | 473 ms: 1.37x faster                                                         |
| Geometric mean          | (ref)                                                  | 1.66x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 51.2 ms: 1.35x faster                                                        |
| nbody          | 93.0 ms                                                | 72.8 ms: 1.28x faster                                                        |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 141 ms: 1.24x faster                                                         |
| regex_compile  | 95.3 ms                                                | 79.1 ms: 1.20x faster                                                        |
| regex_v8       | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                        |
| regex_effbot   | 2.46 ms                                                | 2.33 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 201 us: 1.40x faster                                                         |
| unpickle_pure_python | 194 us                                                 | 148 us: 1.32x faster                                                         |
| tomli_loads          | 1.71 sec                                               | 1.30 sec: 1.31x faster                                                       |
| xml_etree_process    | 46.5 ms                                                | 36.6 ms: 1.27x faster                                                        |
| json_dumps           | 8.11 ms                                                | 7.27 ms: 1.11x faster                                                        |
| xml_etree_generate   | 53.5 ms                                                | 51.4 ms: 1.04x faster                                                        |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.02x faster                                                         |
| json_loads           | 16.4 us                                                | 16.7 us: 1.01x slower                                                        |
| xml_etree_iterparse  | 72.1 ms                                                | 74.1 ms: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.7 ms: 1.81x slower                                                        |
| python_startup_no_site | 7.91 ms                                                | 15.0 ms: 1.90x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.86x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.61 ms: 1.49x faster                                                        |
| django_template | 26.4 ms                                                | 23.8 ms: 1.11x faster                                                        |
| genshi_text     | 17.3 ms                                                | 17.2 ms: 1.01x faster                                                        |
| genshi_xml      | 33.8 ms                                                | 42.0 ms: 1.24x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 102 us: 3.16x faster                                                         |
| async_tree_memoization   | 474 ms                                                 | 257 ms: 1.84x faster                                                         |
| async_tree_none          | 388 ms                                                 | 212 ms: 1.83x faster                                                         |
| deepcopy_memo            | 34.7 us                                                | 19.2 us: 1.81x faster                                                        |
| deltablue                | 4.91 ms                                                | 2.79 ms: 1.76x faster                                                        |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                         |
| deepcopy                 | 272 us                                                 | 163 us: 1.67x faster                                                         |
| async_tree_io            | 980 ms                                                 | 596 ms: 1.64x faster                                                         |
| raytrace                 | 301 ms                                                 | 195 ms: 1.55x faster                                                         |
| richards_super           | 57.8 ms                                                | 38.5 ms: 1.50x faster                                                        |
| mako                     | 9.87 ms                                                | 6.61 ms: 1.49x faster                                                        |
| pylint                   | 277 ms                                                 | 188 ms: 1.47x faster                                                         |
| chaos                    | 65.8 ms                                                | 45.2 ms: 1.45x faster                                                        |
| deepcopy_reduce          | 2.33 us                                                | 1.60 us: 1.45x faster                                                        |
| go                       | 151 ms                                                 | 106 ms: 1.42x faster                                                         |
| richards                 | 48.7 ms                                                | 34.8 ms: 1.40x faster                                                        |
| pickle_pure_python       | 281 us                                                 | 201 us: 1.40x faster                                                         |
| scimark_lu               | 103 ms                                                 | 73.7 ms: 1.39x faster                                                        |
| logging_silent           | 117 ns                                                 | 85.0 ns: 1.38x faster                                                        |
| sqlglot_parse            | 1.24 ms                                                | 903 us: 1.38x faster                                                         |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 473 ms: 1.37x faster                                                         |
| scimark_monte_carlo      | 65.6 ms                                                | 48.0 ms: 1.36x faster                                                        |
| float                    | 69.0 ms                                                | 51.2 ms: 1.35x faster                                                        |
| scimark_sor              | 128 ms                                                 | 96.4 ms: 1.33x faster                                                        |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.72 ms: 1.32x faster                                                        |
| unpickle_pure_python     | 194 us                                                 | 148 us: 1.32x faster                                                         |
| tomli_loads              | 1.71 sec                                               | 1.30 sec: 1.31x faster                                                       |
| sqlglot_transpile        | 1.44 ms                                                | 1.11 ms: 1.31x faster                                                        |
| logging_simple           | 4.45 us                                                | 3.41 us: 1.30x faster                                                        |
| logging_format           | 4.83 us                                                | 3.72 us: 1.30x faster                                                        |
| thrift                   | 572 us                                                 | 442 us: 1.29x faster                                                         |
| nbody                    | 93.0 ms                                                | 72.8 ms: 1.28x faster                                                        |
| crypto_pyaes             | 71.8 ms                                                | 56.3 ms: 1.28x faster                                                        |
| xml_etree_process        | 46.5 ms                                                | 36.6 ms: 1.27x faster                                                        |
| html5lib                 | 42.4 ms                                                | 33.5 ms: 1.27x faster                                                        |
| pprint_safe_repr         | 641 ms                                                 | 507 ms: 1.26x faster                                                         |
| spectral_norm            | 94.8 ms                                                | 75.2 ms: 1.26x faster                                                        |
| pprint_pformat           | 1.30 sec                                               | 1.04 sec: 1.26x faster                                                       |
| pycparser                | 877 ms                                                 | 700 ms: 1.25x faster                                                         |
| regex_dna                | 174 ms                                                 | 141 ms: 1.24x faster                                                         |
| pyflate                  | 427 ms                                                 | 347 ms: 1.23x faster                                                         |
| regex_compile            | 95.3 ms                                                | 79.1 ms: 1.20x faster                                                        |
| dulwich_log              | 35.3 ms                                                | 29.4 ms: 1.20x faster                                                        |
| coroutines               | 20.7 ms                                                | 17.6 ms: 1.18x faster                                                        |
| comprehensions           | 16.9 us                                                | 14.4 us: 1.17x faster                                                        |
| sqlalchemy_declarative   | 73.3 ms                                                | 63.7 ms: 1.15x faster                                                        |
| fannkuch                 | 303 ms                                                 | 264 ms: 1.15x faster                                                         |
| scimark_fft              | 224 ms                                                 | 196 ms: 1.14x faster                                                         |
| generators               | 32.3 ms                                                | 28.6 ms: 1.13x faster                                                        |
| sympy_sum                | 92.2 ms                                                | 82.5 ms: 1.12x faster                                                        |
| json_dumps               | 8.11 ms                                                | 7.27 ms: 1.11x faster                                                        |
| django_template          | 26.4 ms                                                | 23.8 ms: 1.11x faster                                                        |
| hexiom                   | 6.19 ms                                                | 5.60 ms: 1.11x faster                                                        |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                        |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.17 ms: 1.08x faster                                                        |
| docutils                 | 1.73 sec                                               | 1.61 sec: 1.08x faster                                                       |
| regex_v8                 | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                        |
| json                     | 3.08 ms                                                | 2.88 ms: 1.07x faster                                                        |
| regex_effbot             | 2.46 ms                                                | 2.33 ms: 1.06x faster                                                        |
| bench_thread_pool        | 527 us                                                 | 499 us: 1.06x faster                                                         |
| sympy_str                | 165 ms                                                 | 158 ms: 1.04x faster                                                         |
| xml_etree_generate       | 53.5 ms                                                | 51.4 ms: 1.04x faster                                                        |
| sympy_expand             | 269 ms                                                 | 259 ms: 1.04x faster                                                         |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.02x faster                                                         |
| mdp                      | 1.63 sec                                               | 1.61 sec: 1.01x faster                                                       |
| meteor_contest           | 77.7 ms                                                | 76.9 ms: 1.01x faster                                                        |
| genshi_text              | 17.3 ms                                                | 17.2 ms: 1.01x faster                                                        |
| nqueens                  | 63.8 ms                                                | 63.4 ms: 1.01x faster                                                        |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                         |
| sympy_integrate          | 13.1 ms                                                | 13.2 ms: 1.01x slower                                                        |
| 2to3                     | 192 ms                                                 | 193 ms: 1.01x slower                                                         |
| json_loads               | 16.4 us                                                | 16.7 us: 1.01x slower                                                        |
| xml_etree_iterparse      | 72.1 ms                                                | 74.1 ms: 1.03x slower                                                        |
| sqlglot_normalize        | 190 ms                                                 | 197 ms: 1.04x slower                                                         |
| sqlglot_optimize         | 36.8 ms                                                | 39.0 ms: 1.06x slower                                                        |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                                        |
| coverage                 | 41.5 ms                                                | 44.3 ms: 1.07x slower                                                        |
| gc_traversal             | 2.36 ms                                                | 2.93 ms: 1.24x slower                                                        |
| genshi_xml               | 33.8 ms                                                | 42.0 ms: 1.24x slower                                                        |
| async_generators         | 231 ms                                                 | 307 ms: 1.33x slower                                                         |
| telco                    | 3.49 ms                                                | 4.65 ms: 1.33x slower                                                        |
| create_gc_cycles         | 860 us                                                 | 1.33 ms: 1.54x slower                                                        |
| bench_mp_pool            | 37.4 ms                                                | 65.2 ms: 1.74x slower                                                        |
| python_startup           | 10.9 ms                                                | 19.7 ms: 1.81x slower                                                        |
| python_startup_no_site   | 7.91 ms                                                | 15.0 ms: 1.90x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.17x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-darwin-arm64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.181x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.44x