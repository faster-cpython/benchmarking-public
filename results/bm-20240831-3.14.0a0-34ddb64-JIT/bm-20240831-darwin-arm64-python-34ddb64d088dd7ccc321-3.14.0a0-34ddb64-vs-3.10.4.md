# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 180 ms: 1.07x faster                                                  |
| docutils       | 1.73 sec                                               | 1.61 sec: 1.08x faster                                                |
| html5lib       | 42.4 ms                                                | 32.8 ms: 1.29x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 194 ms: 2.01x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.90x faster                                                  |
| async_tree_io           | 980 ms                                                 | 594 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 460 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.4 ms: 1.49x faster                                                 |
| nbody          | 93.0 ms                                                | 63.8 ms: 1.46x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.9 ms: 1.27x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 177 us: 1.59x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.47x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.38x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 34.6 ms: 1.35x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.28 ms: 1.29x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 50.7 ms: 1.06x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| json_loads           | 16.4 us                                                | 17.3 us: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.8 ms: 1.55x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.9 ms: 1.76x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.65x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                 |
| django_template | 26.4 ms                                                | 22.1 ms: 1.19x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 41.2 ms: 1.22x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.0 us: 3.40x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.1 us: 2.15x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.39 ms: 2.06x faster                                                 |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.01x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.90x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.4 ns: 1.88x faster                                                 |
| deepcopy                 | 272 us                                                 | 154 us: 1.76x faster                                                  |
| raytrace                 | 301 ms                                                 | 174 ms: 1.73x faster                                                  |
| async_tree_io            | 980 ms                                                 | 594 ms: 1.65x faster                                                  |
| chaos                    | 65.8 ms                                                | 40.4 ms: 1.63x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 177 us: 1.59x faster                                                  |
| scimark_lu               | 103 ms                                                 | 65.7 ms: 1.57x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.49 us: 1.56x faster                                                 |
| mako                     | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 442 ms: 1.49x faster                                                  |
| float                    | 69.0 ms                                                | 46.4 ms: 1.49x faster                                                 |
| go                       | 151 ms                                                 | 102 ms: 1.48x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.03 us: 1.47x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.8 ms: 1.46x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 857 us: 1.45x faster                                                  |
| logging_format           | 4.83 us                                                | 3.34 us: 1.45x faster                                                 |
| scimark_sor              | 128 ms                                                 | 88.7 ms: 1.44x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 460 ms: 1.41x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 68.3 ms: 1.39x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.1 ms: 1.38x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.38x faster                                                |
| sqlglot_transpile        | 1.44 ms                                                | 1.05 ms: 1.38x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 48.6 ms: 1.35x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 34.6 ms: 1.35x faster                                                 |
| pylint                   | 277 ms                                                 | 207 ms: 1.34x faster                                                  |
| thrift                   | 572 us                                                 | 427 us: 1.34x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.8 us: 1.32x faster                                                 |
| generators               | 32.3 ms                                                | 24.6 ms: 1.32x faster                                                 |
| pyflate                  | 427 ms                                                 | 328 ms: 1.30x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.78 ms: 1.30x faster                                                 |
| html5lib                 | 42.4 ms                                                | 32.8 ms: 1.29x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.28 ms: 1.29x faster                                                 |
| pycparser                | 877 ms                                                 | 681 ms: 1.29x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| regex_compile            | 95.3 ms                                                | 74.9 ms: 1.27x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 1.04 sec: 1.25x faster                                                |
| pprint_safe_repr         | 641 ms                                                 | 511 ms: 1.25x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| dulwich_log              | 35.3 ms                                                | 29.1 ms: 1.21x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 76.4 ms: 1.21x faster                                                 |
| regex_dna                | 174 ms                                                 | 145 ms: 1.21x faster                                                  |
| django_template          | 26.4 ms                                                | 22.1 ms: 1.19x faster                                                 |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.17x faster                                                  |
| richards_super           | 57.8 ms                                                | 49.7 ms: 1.16x faster                                                 |
| fannkuch                 | 303 ms                                                 | 264 ms: 1.15x faster                                                  |
| sympy_str                | 165 ms                                                 | 145 ms: 1.14x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.07 ms: 1.11x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 474 us: 1.11x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.9 ms: 1.11x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.61 sec: 1.08x faster                                                |
| sympy_expand             | 269 ms                                                 | 250 ms: 1.07x faster                                                  |
| nqueens                  | 63.8 ms                                                | 59.5 ms: 1.07x faster                                                 |
| 2to3                     | 192 ms                                                 | 180 ms: 1.07x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 50.7 ms: 1.06x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 73.8 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.57 sec: 1.04x faster                                                |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 184 ms: 1.03x faster                                                  |
| richards                 | 48.7 ms                                                | 47.7 ms: 1.02x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 36.2 ms: 1.02x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.47 ms: 1.01x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 904 us: 1.05x slower                                                  |
| json_loads               | 16.4 us                                                | 17.3 us: 1.06x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.2 ms: 1.09x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 41.2 ms: 1.22x slower                                                 |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 51.6 ms: 1.38x slower                                                 |
| telco                    | 3.49 ms                                                | 4.85 ms: 1.39x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.8 ms: 1.55x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.9 ms: 1.76x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_iterparse, asyncio_websockets, tornado_http
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.00x