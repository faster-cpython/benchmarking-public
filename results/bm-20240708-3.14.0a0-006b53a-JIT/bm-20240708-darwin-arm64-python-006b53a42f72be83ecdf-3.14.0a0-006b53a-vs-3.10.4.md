# Results vs. 3.10.4

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: darwin-arm64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 171 ms: 1.12x faster                                                  |
| docutils       | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                |
| html5lib       | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 232 ms: 2.04x faster                                                  |
| async_tree_none         | 388 ms                                                 | 194 ms: 2.01x faster                                                  |
| async_tree_io           | 980 ms                                                 | 519 ms: 1.89x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 47.2 ms: 1.46x faster                                                 |
| nbody          | 93.0 ms                                                | 64.1 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.5 ms: 1.30x faster                                                 |
| regex_dna      | 174 ms                                                 | 150 ms: 1.16x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.00x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 175 us: 1.61x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.48x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 36.5 ms: 1.27x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.39 ms: 1.27x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 52.5 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 71.3 ms: 1.01x faster                                                 |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.3 ms: 1.41x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.7 ms: 1.60x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.50 ms: 1.52x faster                                                 |
| django_template | 26.4 ms                                                | 21.8 ms: 1.21x faster                                                 |
| genshi_text     | 17.3 ms                                                | 15.8 ms: 1.10x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 39.9 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 96.7 us: 3.34x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.33 ms: 2.11x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.06x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 232 ms: 2.04x faster                                                  |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.01x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.7 ns: 1.90x faster                                                 |
| async_tree_io            | 980 ms                                                 | 519 ms: 1.89x faster                                                  |
| raytrace                 | 301 ms                                                 | 166 ms: 1.82x faster                                                  |
| deepcopy                 | 272 us                                                 | 152 us: 1.79x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.3 ms: 1.67x faster                                                 |
| richards_super           | 57.8 ms                                                | 34.7 ms: 1.67x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 398 ms: 1.66x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 175 us: 1.61x faster                                                  |
| richards                 | 48.7 ms                                                | 31.1 ms: 1.57x faster                                                 |
| pylint                   | 277 ms                                                 | 181 ms: 1.53x faster                                                  |
| mako                     | 9.87 ms                                                | 6.50 ms: 1.52x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 831 us: 1.50x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.56 us: 1.50x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.9 ms: 1.49x faster                                                 |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.48x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.04 us: 1.47x faster                                                 |
| float                    | 69.0 ms                                                | 47.2 ms: 1.46x faster                                                 |
| nbody                    | 93.0 ms                                                | 64.1 ms: 1.45x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.00 ms: 1.44x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| logging_format           | 4.83 us                                                | 3.37 us: 1.43x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.40 ms: 1.41x faster                                                 |
| generators               | 32.3 ms                                                | 23.2 ms: 1.39x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.7 ms: 1.38x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.2 ms: 1.38x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                |
| comprehensions           | 16.9 us                                                | 12.4 us: 1.37x faster                                                 |
| html5lib                 | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                 |
| pyflate                  | 427 ms                                                 | 319 ms: 1.34x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 481 ms: 1.33x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 989 ms: 1.32x faster                                                  |
| thrift                   | 572 us                                                 | 436 us: 1.31x faster                                                  |
| pycparser                | 877 ms                                                 | 675 ms: 1.30x faster                                                  |
| regex_compile            | 95.3 ms                                                | 73.5 ms: 1.30x faster                                                 |
| tornado_http             | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 36.5 ms: 1.27x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.39 ms: 1.27x faster                                                 |
| scimark_sor              | 128 ms                                                 | 102 ms: 1.26x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 73.7 ms: 1.25x faster                                                 |
| scimark_lu               | 103 ms                                                 | 82.6 ms: 1.24x faster                                                 |
| fannkuch                 | 303 ms                                                 | 244 ms: 1.24x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                                |
| django_template          | 26.4 ms                                                | 21.8 ms: 1.21x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.19x faster                                                 |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                                  |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.17x faster                                                  |
| regex_dna                | 174 ms                                                 | 150 ms: 1.16x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.03 ms: 1.13x faster                                                 |
| dask                     | 253 ms                                                 | 225 ms: 1.13x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.45 sec: 1.12x faster                                                |
| 2to3                     | 192 ms                                                 | 171 ms: 1.12x faster                                                  |
| sympy_expand             | 269 ms                                                 | 241 ms: 1.11x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 476 us: 1.11x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.2 ms: 1.11x faster                                                 |
| nqueens                  | 63.8 ms                                                | 57.9 ms: 1.10x faster                                                 |
| genshi_text              | 17.3 ms                                                | 15.8 ms: 1.10x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.7 ms: 1.07x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 179 ms: 1.06x faster                                                  |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.5 ms: 1.02x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 71.3 ms: 1.01x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.00x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 913 us: 1.06x slower                                                  |
| coverage                 | 41.5 ms                                                | 45.9 ms: 1.11x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 39.9 ms: 1.18x slower                                                 |
| async_generators         | 231 ms                                                 | 295 ms: 1.27x slower                                                  |
| telco                    | 3.49 ms                                                | 4.64 ms: 1.33x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 50.1 ms: 1.34x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.3 ms: 1.41x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.7 ms: 1.60x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, asyncio_websockets, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-darwin-arm64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.31x