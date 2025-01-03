# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 4c14f03
- commit date: 2025-01-03
- overall geometric mean: 1.309x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 188 ms: 1.02x faster                                   |
| docutils       | 1.73 sec                                               | 1.47 sec: 1.18x faster                                 |
| html5lib       | 42.4 ms                                                | 29.3 ms: 1.45x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 368 ms: 2.66x faster                                   |
| async_tree_none         | 388 ms                                                 | 161 ms: 2.41x faster                                   |
| async_tree_memoization  | 474 ms                                                 | 201 ms: 2.36x faster                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 414 ms: 1.57x faster                                   |
| Geometric mean          | (ref)                                                  | 2.21x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.3 ms: 1.49x faster                                  |
| nbody          | 93.0 ms                                                | 67.8 ms: 1.37x faster                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.4 ms: 1.41x faster                                  |
| regex_dna      | 174 ms                                                 | 138 ms: 1.27x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.06 ms: 1.20x faster                                  |
| regex_v8       | 17.1 ms                                                | 15.7 ms: 1.09x faster                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 197 us: 1.43x faster                                   |
| unpickle_pure_python | 194 us                                                 | 137 us: 1.42x faster                                   |
| tomli_loads          | 1.71 sec                                               | 1.21 sec: 1.41x faster                                 |
| xml_etree_process    | 46.5 ms                                                | 38.0 ms: 1.22x faster                                  |
| json_dumps           | 8.11 ms                                                | 7.30 ms: 1.11x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                   |
| xml_etree_generate   | 53.5 ms                                                | 52.5 ms: 1.02x faster                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 70.9 ms: 1.02x faster                                  |
| json_loads           | 16.4 us                                                | 16.3 us: 1.01x faster                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.5 ms: 1.61x slower                                  |
| python_startup_no_site | 7.91 ms                                                | 12.8 ms: 1.62x slower                                  |
| Geometric mean         | (ref)                                                  | 1.61x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.13 ms: 1.38x faster                                  |
| genshi_text     | 17.3 ms                                                | 13.5 ms: 1.29x faster                                  |
| django_template | 26.4 ms                                                | 21.0 ms: 1.26x faster                                  |
| genshi_xml      | 33.8 ms                                                | 28.3 ms: 1.19x faster                                  |
| Geometric mean  | (ref)                                                  | 1.28x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 96.1 us: 3.36x faster                                  |
| async_tree_io            | 980 ms                                                 | 368 ms: 2.66x faster                                   |
| async_tree_none          | 388 ms                                                 | 161 ms: 2.41x faster                                   |
| async_tree_memoization   | 474 ms                                                 | 201 ms: 2.36x faster                                   |
| deltablue                | 4.91 ms                                                | 2.35 ms: 2.09x faster                                  |
| go                       | 151 ms                                                 | 78.2 ms: 1.93x faster                                  |
| deepcopy_memo            | 34.7 us                                                | 18.0 us: 1.92x faster                                  |
| deepcopy                 | 272 us                                                 | 150 us: 1.81x faster                                   |
| logging_silent           | 117 ns                                                 | 65.2 ns: 1.80x faster                                  |
| raytrace                 | 301 ms                                                 | 170 ms: 1.77x faster                                   |
| chaos                    | 65.8 ms                                                | 38.0 ms: 1.73x faster                                  |
| pylint                   | 277 ms                                                 | 160 ms: 1.73x faster                                   |
| asyncio_websockets       | 410 ms                                                 | 243 ms: 1.69x faster                                   |
| richards_super           | 57.8 ms                                                | 35.2 ms: 1.64x faster                                  |
| sqlglot_parse            | 1.24 ms                                                | 763 us: 1.63x faster                                   |
| scimark_sor              | 128 ms                                                 | 78.7 ms: 1.63x faster                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 414 ms: 1.57x faster                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 41.9 ms: 1.57x faster                                  |
| sqlglot_transpile        | 1.44 ms                                                | 928 us: 1.55x faster                                   |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                  |
| spectral_norm            | 94.8 ms                                                | 61.8 ms: 1.53x faster                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.56 us: 1.50x faster                                  |
| float                    | 69.0 ms                                                | 46.3 ms: 1.49x faster                                  |
| hexiom                   | 6.19 ms                                                | 4.17 ms: 1.48x faster                                  |
| pyflate                  | 427 ms                                                 | 293 ms: 1.45x faster                                   |
| html5lib                 | 42.4 ms                                                | 29.3 ms: 1.45x faster                                  |
| generators               | 32.3 ms                                                | 22.4 ms: 1.44x faster                                  |
| pickle_pure_python       | 281 us                                                 | 197 us: 1.43x faster                                   |
| scimark_lu               | 103 ms                                                 | 72.2 ms: 1.42x faster                                  |
| unpickle_pure_python     | 194 us                                                 | 137 us: 1.42x faster                                   |
| regex_compile            | 95.3 ms                                                | 67.4 ms: 1.41x faster                                  |
| tomli_loads              | 1.71 sec                                               | 1.21 sec: 1.41x faster                                 |
| pprint_pformat           | 1.30 sec                                               | 926 ms: 1.41x faster                                   |
| logging_simple           | 4.45 us                                                | 3.17 us: 1.40x faster                                  |
| pprint_safe_repr         | 641 ms                                                 | 458 ms: 1.40x faster                                   |
| mako                     | 9.87 ms                                                | 7.13 ms: 1.38x faster                                  |
| logging_format           | 4.83 us                                                | 3.49 us: 1.38x faster                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.42 ms: 1.38x faster                                  |
| pycparser                | 877 ms                                                 | 637 ms: 1.38x faster                                   |
| nbody                    | 93.0 ms                                                | 67.8 ms: 1.37x faster                                  |
| comprehensions           | 16.9 us                                                | 12.5 us: 1.36x faster                                  |
| crypto_pyaes             | 71.8 ms                                                | 53.2 ms: 1.35x faster                                  |
| scimark_fft              | 224 ms                                                 | 172 ms: 1.31x faster                                   |
| thrift                   | 572 us                                                 | 439 us: 1.30x faster                                   |
| dulwich_log              | 35.3 ms                                                | 27.3 ms: 1.29x faster                                  |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                  |
| genshi_text              | 17.3 ms                                                | 13.5 ms: 1.29x faster                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.67 ms: 1.28x faster                                  |
| regex_dna                | 174 ms                                                 | 138 ms: 1.27x faster                                   |
| django_template          | 26.4 ms                                                | 21.0 ms: 1.26x faster                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.2 ms: 1.26x faster                                  |
| sympy_sum                | 92.2 ms                                                | 75.2 ms: 1.23x faster                                  |
| xml_etree_process        | 46.5 ms                                                | 38.0 ms: 1.22x faster                                  |
| fannkuch                 | 303 ms                                                 | 248 ms: 1.22x faster                                   |
| regex_effbot             | 2.46 ms                                                | 2.06 ms: 1.20x faster                                  |
| genshi_xml               | 33.8 ms                                                | 28.3 ms: 1.19x faster                                  |
| docutils                 | 1.73 sec                                               | 1.47 sec: 1.18x faster                                 |
| mypy2                    | 607 ms                                                 | 516 ms: 1.18x faster                                   |
| sympy_str                | 165 ms                                                 | 142 ms: 1.17x faster                                   |
| sympy_integrate          | 13.1 ms                                                | 11.3 ms: 1.16x faster                                  |
| sympy_expand             | 269 ms                                                 | 235 ms: 1.14x faster                                   |
| nqueens                  | 63.8 ms                                                | 56.0 ms: 1.14x faster                                  |
| sqlglot_optimize         | 36.8 ms                                                | 32.5 ms: 1.13x faster                                  |
| bench_thread_pool        | 527 us                                                 | 472 us: 1.12x faster                                   |
| json_dumps               | 8.11 ms                                                | 7.30 ms: 1.11x faster                                  |
| mdp                      | 1.63 sec                                               | 1.49 sec: 1.10x faster                                 |
| regex_v8                 | 17.1 ms                                                | 15.7 ms: 1.09x faster                                  |
| meteor_contest           | 77.7 ms                                                | 71.9 ms: 1.08x faster                                  |
| pathlib                  | 24.5 ms                                                | 22.7 ms: 1.08x faster                                  |
| json                     | 3.08 ms                                                | 2.88 ms: 1.07x faster                                  |
| sqlglot_normalize        | 190 ms                                                 | 179 ms: 1.06x faster                                   |
| xml_etree_parse          | 108 ms                                                 | 102 ms: 1.06x faster                                   |
| 2to3                     | 192 ms                                                 | 188 ms: 1.02x faster                                   |
| xml_etree_generate       | 53.5 ms                                                | 52.5 ms: 1.02x faster                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 70.9 ms: 1.02x faster                                  |
| json_loads               | 16.4 us                                                | 16.3 us: 1.01x faster                                  |
| pidigits                 | 282 ms                                                 | 284 ms: 1.00x slower                                   |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                  |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.09x slower                                  |
| async_generators         | 231 ms                                                 | 276 ms: 1.19x slower                                   |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.31x slower                                  |
| gc_traversal             | 2.36 ms                                                | 3.10 ms: 1.31x slower                                  |
| create_gc_cycles         | 860 us                                                 | 1.29 ms: 1.49x slower                                  |
| bench_mp_pool            | 37.4 ms                                                | 59.6 ms: 1.59x slower                                  |
| python_startup           | 10.9 ms                                                | 17.5 ms: 1.61x slower                                  |
| python_startup_no_site   | 7.91 ms                                                | 12.8 ms: 1.62x slower                                  |
| Geometric mean           | (ref)                                                  | 1.30x faster                                           |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20250103-3.14.0a3+-4c14f03/bm-20250103-darwin-arm64-python-main-3.14.0a3+-4c14f03.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.309x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.35x