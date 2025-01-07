# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: darwin-arm64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.081x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 206 ms: 1.08x slower                                                 |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.15x faster                                               |
| html5lib       | 42.4 ms                                                | 41.7 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 415 ms: 2.36x faster                                                 |
| async_tree_none         | 388 ms                                                 | 191 ms: 2.03x faster                                                 |
| async_tree_memoization  | 474 ms                                                 | 235 ms: 2.01x faster                                                 |
| async_tree_cpu_io_mixed | 649 ms                                                 | 441 ms: 1.47x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.94x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 86.5 ms: 1.08x faster                                                |
| float          | 69.0 ms                                                | 65.8 ms: 1.05x faster                                                |
| pidigits       | 282 ms                                                 | 280 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 136 ms: 1.29x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.10 ms: 1.17x faster                                                |
| regex_compile  | 95.3 ms                                                | 83.2 ms: 1.14x faster                                                |
| regex_v8       | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                |
| Geometric mean | (ref)                                                  | 1.17x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                               |
| xml_etree_iterparse  | 72.1 ms                                                | 66.1 ms: 1.09x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 44.0 ms: 1.06x faster                                                |
| json_dumps           | 8.11 ms                                                | 8.16 ms: 1.01x slower                                                |
| pickle_pure_python   | 281 us                                                 | 289 us: 1.03x slower                                                 |
| unpickle_pure_python | 194 us                                                 | 201 us: 1.03x slower                                                 |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                |
| xml_etree_generate   | 53.5 ms                                                | 58.3 ms: 1.09x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 20.2 ms: 1.86x slower                                                |
| python_startup_no_site | 7.91 ms                                                | 15.2 ms: 1.93x slower                                                |
| Geometric mean         | (ref)                                                  | 1.89x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 17.3 ms                                                | 16.9 ms: 1.03x faster                                                |
| genshi_xml      | 33.8 ms                                                | 34.0 ms: 1.00x slower                                                |
| django_template | 26.4 ms                                                | 27.1 ms: 1.03x slower                                                |
| mako            | 9.87 ms                                                | 11.1 ms: 1.13x slower                                                |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 117 us: 2.75x faster                                                 |
| async_tree_io            | 980 ms                                                 | 415 ms: 2.36x faster                                                 |
| async_tree_none          | 388 ms                                                 | 191 ms: 2.03x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 235 ms: 2.01x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 238 ms: 1.73x faster                                                 |
| deepcopy                 | 272 us                                                 | 174 us: 1.56x faster                                                 |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 22.8 us: 1.53x faster                                                |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 441 ms: 1.47x faster                                                 |
| regex_dna                | 174 ms                                                 | 136 ms: 1.29x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.82 us: 1.28x faster                                                |
| spectral_norm            | 94.8 ms                                                | 75.1 ms: 1.26x faster                                                |
| coroutines               | 20.7 ms                                                | 16.6 ms: 1.25x faster                                                |
| richards_super           | 57.8 ms                                                | 47.4 ms: 1.22x faster                                                |
| pycparser                | 877 ms                                                 | 721 ms: 1.22x faster                                                 |
| regex_effbot             | 2.46 ms                                                | 2.10 ms: 1.17x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                               |
| generators               | 32.3 ms                                                | 27.9 ms: 1.16x faster                                                |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.15x faster                                               |
| chaos                    | 65.8 ms                                                | 57.0 ms: 1.15x faster                                                |
| crypto_pyaes             | 71.8 ms                                                | 62.6 ms: 1.15x faster                                                |
| regex_compile            | 95.3 ms                                                | 83.2 ms: 1.14x faster                                                |
| richards                 | 48.7 ms                                                | 42.7 ms: 1.14x faster                                                |
| pyflate                  | 427 ms                                                 | 386 ms: 1.10x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 83.7 ms: 1.10x faster                                                |
| xml_etree_iterparse      | 72.1 ms                                                | 66.1 ms: 1.09x faster                                                |
| scimark_sor              | 128 ms                                                 | 118 ms: 1.09x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                |
| deltablue                | 4.91 ms                                                | 4.54 ms: 1.08x faster                                                |
| nqueens                  | 63.8 ms                                                | 58.9 ms: 1.08x faster                                                |
| thrift                   | 572 us                                                 | 529 us: 1.08x faster                                                 |
| sqlite_synth             | 1.46 us                                                | 1.35 us: 1.08x faster                                                |
| nbody                    | 93.0 ms                                                | 86.5 ms: 1.08x faster                                                |
| dulwich_log              | 35.3 ms                                                | 32.9 ms: 1.07x faster                                                |
| scimark_lu               | 103 ms                                                 | 95.8 ms: 1.07x faster                                                |
| pathlib                  | 24.5 ms                                                | 22.8 ms: 1.07x faster                                                |
| raytrace                 | 301 ms                                                 | 282 ms: 1.07x faster                                                 |
| sqlalchemy_imperative    | 8.86 ms                                                | 8.29 ms: 1.07x faster                                                |
| xml_etree_parse          | 108 ms                                                 | 102 ms: 1.06x faster                                                 |
| hexiom                   | 6.19 ms                                                | 5.86 ms: 1.06x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 44.0 ms: 1.06x faster                                                |
| scimark_fft              | 224 ms                                                 | 213 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                |
| go                       | 151 ms                                                 | 143 ms: 1.05x faster                                                 |
| float                    | 69.0 ms                                                | 65.8 ms: 1.05x faster                                                |
| fannkuch                 | 303 ms                                                 | 290 ms: 1.04x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 1.26 sec: 1.04x faster                                               |
| pprint_safe_repr         | 641 ms                                                 | 618 ms: 1.04x faster                                                 |
| logging_silent           | 117 ns                                                 | 113 ns: 1.04x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 12.7 ms: 1.03x faster                                                |
| scimark_monte_carlo      | 65.6 ms                                                | 63.9 ms: 1.03x faster                                                |
| genshi_text              | 17.3 ms                                                | 16.9 ms: 1.03x faster                                                |
| logging_simple           | 4.45 us                                                | 4.36 us: 1.02x faster                                                |
| sympy_str                | 165 ms                                                 | 162 ms: 1.02x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.60 sec: 1.02x faster                                               |
| html5lib                 | 42.4 ms                                                | 41.7 ms: 1.02x faster                                                |
| pidigits                 | 282 ms                                                 | 280 ms: 1.01x faster                                                 |
| logging_format           | 4.83 us                                                | 4.81 us: 1.00x faster                                                |
| genshi_xml               | 33.8 ms                                                | 34.0 ms: 1.00x slower                                                |
| comprehensions           | 16.9 us                                                | 17.0 us: 1.01x slower                                                |
| json_dumps               | 8.11 ms                                                | 8.16 ms: 1.01x slower                                                |
| sqlglot_optimize         | 36.8 ms                                                | 37.1 ms: 1.01x slower                                                |
| sqlglot_parse            | 1.24 ms                                                | 1.26 ms: 1.02x slower                                                |
| sqlglot_transpile        | 1.44 ms                                                | 1.48 ms: 1.02x slower                                                |
| sqlalchemy_declarative   | 73.3 ms                                                | 75.1 ms: 1.03x slower                                                |
| meteor_contest           | 77.7 ms                                                | 79.9 ms: 1.03x slower                                                |
| django_template          | 26.4 ms                                                | 27.1 ms: 1.03x slower                                                |
| sympy_expand             | 269 ms                                                 | 276 ms: 1.03x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 289 us: 1.03x slower                                                 |
| unpickle_pure_python     | 194 us                                                 | 201 us: 1.03x slower                                                 |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.61 ms: 1.06x slower                                                |
| sqlglot_normalize        | 190 ms                                                 | 203 ms: 1.07x slower                                                 |
| 2to3                     | 192 ms                                                 | 206 ms: 1.08x slower                                                 |
| xml_etree_generate       | 53.5 ms                                                | 58.3 ms: 1.09x slower                                                |
| gc_traversal             | 2.36 ms                                                | 2.64 ms: 1.12x slower                                                |
| mako                     | 9.87 ms                                                | 11.1 ms: 1.13x slower                                                |
| coverage                 | 41.5 ms                                                | 51.9 ms: 1.25x slower                                                |
| async_generators         | 231 ms                                                 | 295 ms: 1.27x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 1.15 ms: 1.34x slower                                                |
| telco                    | 3.49 ms                                                | 5.04 ms: 1.44x slower                                                |
| bench_thread_pool        | 527 us                                                 | 817 us: 1.55x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 68.4 ms: 1.83x slower                                                |
| python_startup           | 10.9 ms                                                | 20.2 ms: 1.86x slower                                                |
| python_startup_no_site   | 7.91 ms                                                | 15.2 ms: 1.93x slower                                                |
| Geometric mean           | (ref)                                                  | 1.07x faster                                                         |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-darwin-arm64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.53x