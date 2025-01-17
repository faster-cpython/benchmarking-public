# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.221x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 203 ms: 1.06x slower                                                   |
| docutils       | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                 |
| html5lib       | 42.4 ms                                                | 33.3 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 252 ms: 1.88x faster                                                   |
| async_tree_none         | 388 ms                                                 | 212 ms: 1.83x faster                                                   |
| async_tree_io           | 980 ms                                                 | 609 ms: 1.61x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 474 ms: 1.37x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.66x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.5 ms: 1.47x faster                                                  |
| float          | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 71.9 ms: 1.33x faster                                                  |
| regex_dna      | 174 ms                                                 | 135 ms: 1.29x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.01 ms: 1.22x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                 | 126 us: 1.55x faster                                                   |
| pickle_pure_python   | 281 us                                                 | 195 us: 1.44x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.35x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 35.7 ms: 1.30x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.21 ms: 1.12x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 50.7 ms: 1.06x faster                                                  |
| json_loads           | 16.4 us                                                | 16.5 us: 1.01x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 74.5 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 20.5 ms: 1.89x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 15.7 ms: 1.98x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.93x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.24 ms: 1.58x faster                                                  |
| django_template | 26.4 ms                                                | 23.0 ms: 1.15x faster                                                  |
| genshi_text     | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 39.3 ms: 1.16x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 99.1 us: 3.26x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.5 us: 1.98x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.61 ms: 1.88x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 252 ms: 1.88x faster                                                   |
| async_tree_none          | 388 ms                                                 | 212 ms: 1.83x faster                                                   |
| pylint                   | 277 ms                                                 | 161 ms: 1.72x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy                 | 272 us                                                 | 161 us: 1.69x faster                                                   |
| raytrace                 | 301 ms                                                 | 183 ms: 1.64x faster                                                   |
| async_tree_io            | 980 ms                                                 | 609 ms: 1.61x faster                                                   |
| mako                     | 9.87 ms                                                | 6.24 ms: 1.58x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 126 us: 1.55x faster                                                   |
| logging_silent           | 117 ns                                                 | 76.5 ns: 1.53x faster                                                  |
| chaos                    | 65.8 ms                                                | 43.4 ms: 1.52x faster                                                  |
| richards_super           | 57.8 ms                                                | 38.4 ms: 1.50x faster                                                  |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                   |
| scimark_lu               | 103 ms                                                 | 69.3 ms: 1.48x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.58 us: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.47x faster                                                  |
| scimark_sor              | 128 ms                                                 | 87.8 ms: 1.46x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 45.3 ms: 1.45x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 195 us: 1.44x faster                                                   |
| richards                 | 48.7 ms                                                | 34.2 ms: 1.43x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 880 us: 1.41x faster                                                   |
| float                    | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 474 ms: 1.37x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 69.6 ms: 1.36x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.06 ms: 1.36x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.35x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 482 ms: 1.33x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 982 ms: 1.33x faster                                                   |
| regex_compile            | 95.3 ms                                                | 71.9 ms: 1.33x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.69 ms: 1.32x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 54.8 ms: 1.31x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.40 us: 1.31x faster                                                  |
| pyflate                  | 427 ms                                                 | 327 ms: 1.30x faster                                                   |
| xml_etree_process        | 46.5 ms                                                | 35.7 ms: 1.30x faster                                                  |
| logging_format           | 4.83 us                                                | 3.72 us: 1.30x faster                                                  |
| thrift                   | 572 us                                                 | 442 us: 1.29x faster                                                   |
| regex_dna                | 174 ms                                                 | 135 ms: 1.29x faster                                                   |
| pycparser                | 877 ms                                                 | 681 ms: 1.29x faster                                                   |
| html5lib                 | 42.4 ms                                                | 33.3 ms: 1.27x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.97 ms: 1.25x faster                                                  |
| comprehensions           | 16.9 us                                                | 13.7 us: 1.24x faster                                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 59.6 ms: 1.23x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.01 ms: 1.22x faster                                                  |
| scimark_fft              | 224 ms                                                 | 186 ms: 1.21x faster                                                   |
| generators               | 32.3 ms                                                | 26.8 ms: 1.21x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 76.9 ms: 1.20x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.9 ms: 1.18x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.5 ms: 1.18x faster                                                  |
| django_template          | 26.4 ms                                                | 23.0 ms: 1.15x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                 |
| sympy_str                | 165 ms                                                 | 147 ms: 1.13x faster                                                   |
| json_dumps               | 8.11 ms                                                | 7.21 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.07 ms: 1.12x faster                                                  |
| sympy_expand             | 269 ms                                                 | 248 ms: 1.09x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 12.1 ms: 1.08x faster                                                  |
| json                     | 3.08 ms                                                | 2.85 ms: 1.08x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.7 ms: 1.08x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 492 us: 1.07x faster                                                   |
| fannkuch                 | 303 ms                                                 | 284 ms: 1.07x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 73.3 ms: 1.06x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 50.7 ms: 1.06x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 35.3 ms: 1.04x faster                                                  |
| genshi_text              | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.59 sec: 1.03x faster                                                 |
| nqueens                  | 63.8 ms                                                | 62.6 ms: 1.02x faster                                                  |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| json_loads               | 16.4 us                                                | 16.5 us: 1.01x slower                                                  |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 74.5 ms: 1.03x slower                                                  |
| sqlglot_normalize        | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| 2to3                     | 192 ms                                                 | 203 ms: 1.06x slower                                                   |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.9 ms: 1.08x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 39.3 ms: 1.16x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.96 ms: 1.25x slower                                                  |
| telco                    | 3.49 ms                                                | 4.54 ms: 1.30x slower                                                  |
| async_generators         | 231 ms                                                 | 304 ms: 1.31x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 1.32 ms: 1.53x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 61.9 ms: 1.65x slower                                                  |
| python_startup           | 10.9 ms                                                | 20.5 ms: 1.89x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 15.7 ms: 1.98x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.221x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.36x