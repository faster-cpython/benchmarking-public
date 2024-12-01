# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.242x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 169 ms: 1.13x faster                                                   |
| docutils       | 1.73 sec                                               | 1.44 sec: 1.20x faster                                                 |
| html5lib       | 42.4 ms                                                | 31.3 ms: 1.35x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 253 ms: 1.87x faster                                                   |
| async_tree_none         | 388 ms                                                 | 211 ms: 1.84x faster                                                   |
| async_tree_io           | 980 ms                                                 | 611 ms: 1.60x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 472 ms: 1.37x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.66x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 68.6 ms: 1.36x faster                                                  |
| float          | 69.0 ms                                                | 53.3 ms: 1.29x faster                                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.1 ms: 1.32x faster                                                  |
| regex_dna      | 174 ms                                                 | 134 ms: 1.30x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.08 ms: 1.18x faster                                                  |
| regex_v8       | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 207 us: 1.36x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 154 us: 1.26x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 39.2 ms: 1.19x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.53 sec: 1.11x faster                                                 |
| json_dumps           | 8.11 ms                                                | 7.28 ms: 1.11x faster                                                  |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| xml_etree_generate   | 53.5 ms                                                | 54.3 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 76.9 ms: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 20.3 ms: 1.87x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 15.5 ms: 1.96x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.91x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.13 ms: 1.39x faster                                                  |
| django_template | 26.4 ms                                                | 20.8 ms: 1.27x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.4 ms: 1.20x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 31.0 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 98.2 us: 3.29x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.47 ms: 1.99x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 18.2 us: 1.90x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 253 ms: 1.87x faster                                                   |
| async_tree_none          | 388 ms                                                 | 211 ms: 1.84x faster                                                   |
| pylint                   | 277 ms                                                 | 152 ms: 1.83x faster                                                   |
| deepcopy                 | 272 us                                                 | 152 us: 1.79x faster                                                   |
| raytrace                 | 301 ms                                                 | 171 ms: 1.76x faster                                                   |
| go                       | 151 ms                                                 | 87.6 ms: 1.72x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| chaos                    | 65.8 ms                                                | 39.4 ms: 1.67x faster                                                  |
| logging_silent           | 117 ns                                                 | 70.3 ns: 1.67x faster                                                  |
| async_tree_io            | 980 ms                                                 | 611 ms: 1.60x faster                                                   |
| richards_super           | 57.8 ms                                                | 37.0 ms: 1.56x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 808 us: 1.54x faster                                                   |
| sqlglot_transpile        | 1.44 ms                                                | 983 us: 1.47x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 1.59 us: 1.46x faster                                                  |
| richards                 | 48.7 ms                                                | 33.5 ms: 1.45x faster                                                  |
| generators               | 32.3 ms                                                | 22.5 ms: 1.44x faster                                                  |
| scimark_lu               | 103 ms                                                 | 72.4 ms: 1.42x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 46.5 ms: 1.41x faster                                                  |
| mako                     | 9.87 ms                                                | 7.13 ms: 1.39x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.44 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 472 ms: 1.37x faster                                                   |
| hexiom                   | 6.19 ms                                                | 4.55 ms: 1.36x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 207 us: 1.36x faster                                                   |
| nbody                    | 93.0 ms                                                | 68.6 ms: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.3 ms: 1.35x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.29 us: 1.35x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.5 us: 1.35x faster                                                  |
| logging_format           | 4.83 us                                                | 3.59 us: 1.34x faster                                                  |
| pycparser                | 877 ms                                                 | 658 ms: 1.33x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 984 ms: 1.32x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 54.3 ms: 1.32x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 484 ms: 1.32x faster                                                   |
| thrift                   | 572 us                                                 | 433 us: 1.32x faster                                                   |
| regex_compile            | 95.3 ms                                                | 72.1 ms: 1.32x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 72.7 ms: 1.30x faster                                                  |
| regex_dna                | 174 ms                                                 | 134 ms: 1.30x faster                                                   |
| float                    | 69.0 ms                                                | 53.3 ms: 1.29x faster                                                  |
| scimark_sor              | 128 ms                                                 | 101 ms: 1.28x faster                                                   |
| django_template          | 26.4 ms                                                | 20.8 ms: 1.27x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 154 us: 1.26x faster                                                   |
| pyflate                  | 427 ms                                                 | 338 ms: 1.26x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 73.0 ms: 1.26x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 28.1 ms: 1.26x faster                                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.6 ms: 1.25x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.4 ms: 1.20x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.44 sec: 1.20x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 39.2 ms: 1.19x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.08 ms: 1.18x faster                                                  |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                                   |
| coroutines               | 20.7 ms                                                | 17.6 ms: 1.18x faster                                                  |
| scimark_fft              | 224 ms                                                 | 195 ms: 1.15x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 11.5 ms: 1.14x faster                                                  |
| sympy_expand             | 269 ms                                                 | 236 ms: 1.14x faster                                                   |
| 2to3                     | 192 ms                                                 | 169 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.03 ms: 1.13x faster                                                  |
| fannkuch                 | 303 ms                                                 | 269 ms: 1.12x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 33.0 ms: 1.12x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.53 sec: 1.11x faster                                                 |
| json_dumps               | 8.11 ms                                                | 7.28 ms: 1.11x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 475 us: 1.11x faster                                                   |
| genshi_xml               | 33.8 ms                                                | 31.0 ms: 1.09x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                  |
| nqueens                  | 63.8 ms                                                | 59.1 ms: 1.08x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                  |
| json                     | 3.08 ms                                                | 2.87 ms: 1.07x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.4 ms: 1.07x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.52 sec: 1.07x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 181 ms: 1.05x faster                                                   |
| pidigits                 | 282 ms                                                 | 284 ms: 1.00x slower                                                   |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| xml_etree_generate       | 53.5 ms                                                | 54.3 ms: 1.01x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.2 ms: 1.06x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 76.9 ms: 1.07x slower                                                  |
| async_generators         | 231 ms                                                 | 287 ms: 1.24x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.95 ms: 1.25x slower                                                  |
| telco                    | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.30 ms: 1.52x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 61.7 ms: 1.65x slower                                                  |
| python_startup           | 10.9 ms                                                | 20.3 ms: 1.87x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 15.5 ms: 1.96x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.242x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.33x