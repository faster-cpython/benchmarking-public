# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: tail_call
- machine: darwin-arm64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.396x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 151 ms: 1.27x faster                                                  |
| docutils       | 1.73 sec                                               | 1.37 sec: 1.27x faster                                                |
| html5lib       | 42.4 ms                                                | 29.0 ms: 1.46x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 348 ms: 2.81x faster                                                  |
| async_tree_none         | 388 ms                                                 | 152 ms: 2.55x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 191 ms: 2.48x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 401 ms: 1.62x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.32x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 43.4 ms: 1.59x faster                                                 |
| nbody          | 93.0 ms                                                | 60.2 ms: 1.54x faster                                                 |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 61.9 ms: 1.54x faster                                                 |
| regex_dna      | 174 ms                                                 | 138 ms: 1.26x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.05 ms: 1.20x faster                                                 |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                 | 120 us: 1.62x faster                                                  |
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.14 sec: 1.50x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 33.9 ms: 1.37x faster                                                 |
| json_dumps           | 8.11 ms                                                | 7.08 ms: 1.15x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 48.4 ms: 1.10x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 97.7 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 68.8 ms: 1.05x faster                                                 |
| json_loads           | 16.4 us                                                | 16.1 us: 1.02x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.6 ms: 1.71x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.6 ms: 1.72x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.72x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.91 ms: 1.43x faster                                                 |
| genshi_text     | 17.3 ms                                                | 12.4 ms: 1.39x faster                                                 |
| django_template | 26.4 ms                                                | 19.1 ms: 1.38x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 26.5 ms: 1.28x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 89.7 us: 3.60x faster                                                 |
| async_tree_io            | 980 ms                                                 | 348 ms: 2.81x faster                                                  |
| async_tree_none          | 388 ms                                                 | 152 ms: 2.55x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 191 ms: 2.48x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.05 ms: 2.40x faster                                                 |
| go                       | 151 ms                                                 | 70.9 ms: 2.13x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.10x faster                                                 |
| logging_silent           | 117 ns                                                 | 57.8 ns: 2.03x faster                                                 |
| raytrace                 | 301 ms                                                 | 152 ms: 1.98x faster                                                  |
| deepcopy                 | 272 us                                                 | 140 us: 1.95x faster                                                  |
| chaos                    | 65.8 ms                                                | 34.5 ms: 1.91x faster                                                 |
| generators               | 32.3 ms                                                | 17.2 ms: 1.88x faster                                                 |
| richards_super           | 57.8 ms                                                | 30.8 ms: 1.88x faster                                                 |
| pylint                   | 277 ms                                                 | 150 ms: 1.84x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 684 us: 1.82x faster                                                  |
| richards                 | 48.7 ms                                                | 27.4 ms: 1.78x faster                                                 |
| scimark_sor              | 128 ms                                                 | 72.7 ms: 1.76x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 37.6 ms: 1.74x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 840 us: 1.72x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                  |
| hexiom                   | 6.19 ms                                                | 3.71 ms: 1.67x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 120 us: 1.62x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 401 ms: 1.62x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.46 us: 1.60x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 59.4 ms: 1.60x faster                                                 |
| scimark_lu               | 103 ms                                                 | 64.6 ms: 1.59x faster                                                 |
| float                    | 69.0 ms                                                | 43.4 ms: 1.59x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.7 us: 1.58x faster                                                 |
| nbody                    | 93.0 ms                                                | 60.2 ms: 1.54x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 46.6 ms: 1.54x faster                                                 |
| regex_compile            | 95.3 ms                                                | 61.9 ms: 1.54x faster                                                 |
| logging_simple           | 4.45 us                                                | 2.92 us: 1.52x faster                                                 |
| pyflate                  | 427 ms                                                 | 282 ms: 1.51x faster                                                  |
| logging_format           | 4.83 us                                                | 3.23 us: 1.50x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.14 sec: 1.50x faster                                                |
| pprint_pformat           | 1.30 sec                                               | 875 ms: 1.49x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 437 ms: 1.47x faster                                                  |
| html5lib                 | 42.4 ms                                                | 29.0 ms: 1.46x faster                                                 |
| pycparser                | 877 ms                                                 | 609 ms: 1.44x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.15 ms: 1.44x faster                                                 |
| mako                     | 9.87 ms                                                | 6.91 ms: 1.43x faster                                                 |
| coroutines               | 20.7 ms                                                | 14.7 ms: 1.41x faster                                                 |
| genshi_text              | 17.3 ms                                                | 12.4 ms: 1.39x faster                                                 |
| django_template          | 26.4 ms                                                | 19.1 ms: 1.38x faster                                                 |
| thrift                   | 572 us                                                 | 416 us: 1.37x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 33.9 ms: 1.37x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 26.2 ms: 1.35x faster                                                 |
| scimark_fft              | 224 ms                                                 | 167 ms: 1.35x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.3 ms: 1.33x faster                                                 |
| sqlalchemy_declarative   | 73.3 ms                                                | 55.3 ms: 1.33x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.60 ms: 1.32x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.2 ms: 1.29x faster                                                 |
| genshi_xml               | 33.8 ms                                                | 26.5 ms: 1.28x faster                                                 |
| sympy_str                | 165 ms                                                 | 130 ms: 1.27x faster                                                  |
| 2to3                     | 192 ms                                                 | 151 ms: 1.27x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.37 sec: 1.27x faster                                                |
| fannkuch                 | 303 ms                                                 | 240 ms: 1.26x faster                                                  |
| regex_dna                | 174 ms                                                 | 138 ms: 1.26x faster                                                  |
| nqueens                  | 63.8 ms                                                | 50.7 ms: 1.26x faster                                                 |
| sympy_expand             | 269 ms                                                 | 220 ms: 1.22x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 30.4 ms: 1.21x faster                                                 |
| regex_effbot             | 2.46 ms                                                | 2.05 ms: 1.20x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 454 us: 1.16x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.08 ms: 1.15x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 70.0 ms: 1.11x faster                                                 |
| json                     | 3.08 ms                                                | 2.78 ms: 1.11x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 48.4 ms: 1.10x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 97.7 ms: 1.10x faster                                                 |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 68.8 ms: 1.05x faster                                                 |
| json_loads               | 16.4 us                                                | 16.1 us: 1.02x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                 |
| pidigits                 | 282 ms                                                 | 280 ms: 1.01x faster                                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.08x slower                                                 |
| async_generators         | 231 ms                                                 | 279 ms: 1.21x slower                                                  |
| telco                    | 3.49 ms                                                | 4.41 ms: 1.26x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 3.06 ms: 1.30x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 1.27 ms: 1.47x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 59.9 ms: 1.60x slower                                                 |
| python_startup           | 10.9 ms                                                | 18.6 ms: 1.71x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.6 ms: 1.72x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                          |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20250107-3.14.0a3+-f1d3190/bm-20250107-darwin-arm64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.396x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.32x