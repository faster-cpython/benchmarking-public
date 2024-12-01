# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.023x slower
- HPT reliability: 99.46%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 221 ms: 1.15x slower                                                   |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.11x faster                                                 |
| html5lib       | 42.4 ms                                                | 45.9 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 481 ms: 2.04x faster                                                   |
| async_tree_none         | 388 ms                                                 | 216 ms: 1.80x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 266 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 472 ms: 1.38x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 93.0 ms                                                | 94.7 ms: 1.02x slower                                                  |
| float          | 69.0 ms                                                | 86.5 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 136 ms: 1.28x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.07 ms: 1.19x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                  |
| regex_compile  | 95.3 ms                                                | 97.1 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 99.7 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 69.0 ms: 1.05x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.75 sec: 1.03x slower                                                 |
| xml_etree_process    | 46.5 ms                                                | 48.1 ms: 1.03x slower                                                  |
| json_dumps           | 8.11 ms                                                | 8.39 ms: 1.04x slower                                                  |
| json_loads           | 16.4 us                                                | 17.6 us: 1.07x slower                                                  |
| pickle_pure_python   | 281 us                                                 | 312 us: 1.11x slower                                                   |
| xml_etree_generate   | 53.5 ms                                                | 60.3 ms: 1.13x slower                                                  |
| unpickle_pure_python | 194 us                                                 | 230 us: 1.18x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 22.8 ms: 2.10x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 17.8 ms: 2.25x slower                                                  |
| Geometric mean         | (ref)                                                  | 2.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 33.8 ms                                                | 37.7 ms: 1.11x slower                                                  |
| genshi_text     | 17.3 ms                                                | 19.6 ms: 1.13x slower                                                  |
| django_template | 26.4 ms                                                | 30.6 ms: 1.16x slower                                                  |
| mako            | 9.87 ms                                                | 12.6 ms: 1.27x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.17x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 123 us: 2.62x faster                                                   |
| async_tree_io            | 980 ms                                                 | 481 ms: 2.04x faster                                                   |
| async_tree_none          | 388 ms                                                 | 216 ms: 1.80x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 266 ms: 1.78x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 238 ms: 1.72x faster                                                   |
| pylint                   | 277 ms                                                 | 197 ms: 1.40x faster                                                   |
| deepcopy                 | 272 us                                                 | 196 us: 1.38x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 472 ms: 1.38x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 26.2 us: 1.33x faster                                                  |
| regex_dna                | 174 ms                                                 | 136 ms: 1.28x faster                                                   |
| regex_effbot             | 2.46 ms                                                | 2.07 ms: 1.19x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 80.1 ms: 1.18x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.01 us: 1.16x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.11x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 99.7 ms: 1.08x faster                                                  |
| generators               | 32.3 ms                                                | 30.0 ms: 1.08x faster                                                  |
| coroutines               | 20.7 ms                                                | 19.3 ms: 1.07x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 68.0 ms: 1.06x faster                                                  |
| pycparser                | 877 ms                                                 | 830 ms: 1.06x faster                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 69.0 ms: 1.05x faster                                                  |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                  |
| chaos                    | 65.8 ms                                                | 64.1 ms: 1.03x faster                                                  |
| json                     | 3.08 ms                                                | 3.05 ms: 1.01x faster                                                  |
| sqlite_synth             | 1.46 us                                                | 1.45 us: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 280 ms: 1.01x faster                                                   |
| scimark_fft              | 224 ms                                                 | 228 ms: 1.01x slower                                                   |
| nbody                    | 93.0 ms                                                | 94.7 ms: 1.02x slower                                                  |
| regex_compile            | 95.3 ms                                                | 97.1 ms: 1.02x slower                                                  |
| pyflate                  | 427 ms                                                 | 435 ms: 1.02x slower                                                   |
| tomli_loads              | 1.71 sec                                               | 1.75 sec: 1.03x slower                                                 |
| mdp                      | 1.63 sec                                               | 1.68 sec: 1.03x slower                                                 |
| richards_super           | 57.8 ms                                                | 59.5 ms: 1.03x slower                                                  |
| deltablue                | 4.91 ms                                                | 5.07 ms: 1.03x slower                                                  |
| xml_etree_process        | 46.5 ms                                                | 48.1 ms: 1.03x slower                                                  |
| json_dumps               | 8.11 ms                                                | 8.39 ms: 1.04x slower                                                  |
| scimark_sor              | 128 ms                                                 | 133 ms: 1.04x slower                                                   |
| dulwich_log              | 35.3 ms                                                | 36.7 ms: 1.04x slower                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 9.20 ms: 1.04x slower                                                  |
| fannkuch                 | 303 ms                                                 | 315 ms: 1.04x slower                                                   |
| richards                 | 48.7 ms                                                | 50.8 ms: 1.04x slower                                                  |
| logging_silent           | 117 ns                                                 | 122 ns: 1.04x slower                                                   |
| raytrace                 | 301 ms                                                 | 316 ms: 1.05x slower                                                   |
| comprehensions           | 16.9 us                                                | 17.9 us: 1.05x slower                                                  |
| go                       | 151 ms                                                 | 161 ms: 1.07x slower                                                   |
| json_loads               | 16.4 us                                                | 17.6 us: 1.07x slower                                                  |
| meteor_contest           | 77.7 ms                                                | 83.5 ms: 1.07x slower                                                  |
| thrift                   | 572 us                                                 | 615 us: 1.08x slower                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 70.8 ms: 1.08x slower                                                  |
| html5lib                 | 42.4 ms                                                | 45.9 ms: 1.08x slower                                                  |
| hexiom                   | 6.19 ms                                                | 6.72 ms: 1.08x slower                                                  |
| pprint_safe_repr         | 641 ms                                                 | 698 ms: 1.09x slower                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.74 ms: 1.09x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.42 sec: 1.09x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 312 us: 1.11x slower                                                   |
| genshi_xml               | 33.8 ms                                                | 37.7 ms: 1.11x slower                                                  |
| sympy_integrate          | 13.1 ms                                                | 14.6 ms: 1.12x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.64 ms: 1.12x slower                                                  |
| genshi_text              | 17.3 ms                                                | 19.6 ms: 1.13x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 60.3 ms: 1.13x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 41.9 ms: 1.14x slower                                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 84.2 ms: 1.15x slower                                                  |
| 2to3                     | 192 ms                                                 | 221 ms: 1.15x slower                                                   |
| django_template          | 26.4 ms                                                | 30.6 ms: 1.16x slower                                                  |
| logging_simple           | 4.45 us                                                | 5.22 us: 1.17x slower                                                  |
| logging_format           | 4.83 us                                                | 5.67 us: 1.17x slower                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.70 ms: 1.18x slower                                                  |
| sqlglot_normalize        | 190 ms                                                 | 224 ms: 1.18x slower                                                   |
| unpickle_pure_python     | 194 us                                                 | 230 us: 1.18x slower                                                   |
| scimark_lu               | 103 ms                                                 | 122 ms: 1.19x slower                                                   |
| sqlglot_parse            | 1.24 ms                                                | 1.50 ms: 1.21x slower                                                  |
| sympy_str                | 165 ms                                                 | 202 ms: 1.22x slower                                                   |
| float                    | 69.0 ms                                                | 86.5 ms: 1.25x slower                                                  |
| mako                     | 9.87 ms                                                | 12.6 ms: 1.27x slower                                                  |
| coverage                 | 41.5 ms                                                | 53.8 ms: 1.30x slower                                                  |
| async_generators         | 231 ms                                                 | 309 ms: 1.33x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 1.15 ms: 1.34x slower                                                  |
| sympy_sum                | 92.2 ms                                                | 125 ms: 1.35x slower                                                   |
| sympy_expand             | 269 ms                                                 | 379 ms: 1.41x slower                                                   |
| telco                    | 3.49 ms                                                | 5.03 ms: 1.44x slower                                                  |
| bench_thread_pool        | 527 us                                                 | 793 us: 1.50x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 74.1 ms: 1.98x slower                                                  |
| python_startup           | 10.9 ms                                                | 22.8 ms: 2.10x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 17.8 ms: 2.25x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (1): nqueens
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 99.46% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.51x