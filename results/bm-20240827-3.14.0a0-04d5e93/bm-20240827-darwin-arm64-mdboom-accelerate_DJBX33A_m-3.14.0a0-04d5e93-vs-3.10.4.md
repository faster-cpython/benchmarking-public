# Results vs. 3.10.4

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: darwin-arm64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 158 ms: 1.21x faster                                                  |
| docutils       | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                |
| html5lib       | 42.4 ms                                                | 31.4 ms: 1.35x faster                                                 |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 192 ms: 2.02x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.90x faster                                                  |
| async_tree_io           | 980 ms                                                 | 594 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.1 ms: 1.55x faster                                                 |
| float          | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.2 ms: 1.42x faster                                                 |
| regex_dna      | 174 ms                                                 | 146 ms: 1.19x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 184 us: 1.53x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.42 ms: 1.26x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.43 sec: 1.19x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.9 ms: 1.47x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.2 ms: 1.67x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.56x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.91 ms: 1.43x faster                                                 |
| django_template | 26.4 ms                                                | 19.8 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.4 us: 3.53x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.12 ms: 2.31x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.9 us: 2.05x faster                                                 |
| async_tree_none          | 388 ms                                                 | 192 ms: 2.02x faster                                                  |
| raytrace                 | 301 ms                                                 | 150 ms: 2.01x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.1 ns: 1.92x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.90x faster                                                  |
| deepcopy                 | 272 us                                                 | 144 us: 1.89x faster                                                  |
| chaos                    | 65.8 ms                                                | 34.9 ms: 1.88x faster                                                 |
| richards_super           | 57.8 ms                                                | 34.3 ms: 1.69x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 745 us: 1.67x faster                                                  |
| async_tree_io            | 980 ms                                                 | 594 ms: 1.65x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 401 ms: 1.64x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.3 us: 1.64x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 900 us: 1.60x faster                                                  |
| richards                 | 48.7 ms                                                | 31.1 ms: 1.57x faster                                                 |
| generators               | 32.3 ms                                                | 20.8 ms: 1.56x faster                                                 |
| nbody                    | 93.0 ms                                                | 60.1 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                 |
| scimark_lu               | 103 ms                                                 | 66.8 ms: 1.54x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.06 ms: 1.53x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 184 us: 1.53x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.2 ms: 1.52x faster                                                 |
| pylint                   | 277 ms                                                 | 183 ms: 1.51x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.06 us: 1.45x faster                                                 |
| logging_format           | 4.83 us                                                | 3.37 us: 1.43x faster                                                 |
| mako                     | 9.87 ms                                                | 6.91 ms: 1.43x faster                                                 |
| float                    | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                 |
| regex_compile            | 95.3 ms                                                | 67.2 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 50.8 ms: 1.41x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.1 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 454 ms: 1.41x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 931 ms: 1.40x faster                                                  |
| go                       | 151 ms                                                 | 108 ms: 1.40x faster                                                  |
| scimark_sor              | 128 ms                                                 | 93.0 ms: 1.38x faster                                                 |
| thrift                   | 572 us                                                 | 419 us: 1.37x faster                                                  |
| pycparser                | 877 ms                                                 | 644 ms: 1.36x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.4 ms: 1.35x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 68.9 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 319 ms: 1.34x faster                                                  |
| django_template          | 26.4 ms                                                | 19.8 ms: 1.34x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 26.9 ms: 1.31x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.42 ms: 1.26x faster                                                 |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.78 ms: 1.23x faster                                                 |
| 2to3                     | 192 ms                                                 | 158 ms: 1.21x faster                                                  |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.2 ms: 1.20x faster                                                 |
| regex_dna                | 174 ms                                                 | 146 ms: 1.19x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.43 sec: 1.19x faster                                                |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.18x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 31.2 ms: 1.18x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 449 us: 1.18x faster                                                  |
| fannkuch                 | 303 ms                                                 | 260 ms: 1.16x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                                |
| genshi_xml               | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.1 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.47 ms: 1.01x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 73.7 ms: 1.02x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 901 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.8 ms: 1.08x slower                                                 |
| async_generators         | 231 ms                                                 | 280 ms: 1.21x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.6 ms: 1.30x slower                                                 |
| telco                    | 3.49 ms                                                | 4.69 ms: 1.34x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.9 ms: 1.47x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.2 ms: 1.67x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, pidigits, xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240827-3.14.0a0-04d5e93/bm-20240827-darwin-arm64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.70x