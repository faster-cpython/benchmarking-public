# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.16x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 0.77x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 254 ms: 1.33x slower                                                  |
| docutils       | 1.73 sec                                               | 1.79 sec: 1.04x slower                                                |
| html5lib       | 42.4 ms                                                | 52.3 ms: 1.24x slower                                                 |
| tornado_http   | 86.7 ms                                                | 110 ms: 1.27x slower                                                  |
| Geometric mean | (ref)                                                  | 1.21x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 550 ms: 1.78x faster                                                  |
| async_tree_none         | 388 ms                                                 | 243 ms: 1.60x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 300 ms: 1.58x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 504 ms: 1.29x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.55x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 69.0 ms                                                | 98.7 ms: 1.43x slower                                                 |
| nbody          | 93.0 ms                                                | 159 ms: 1.71x slower                                                  |
| Geometric mean | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 139 ms: 1.26x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| regex_compile  | 95.3 ms                                                | 125 ms: 1.32x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| json_dumps           | 8.11 ms                                                | 8.12 ms: 1.00x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 78.2 ms: 1.08x slower                                                 |
| json_loads           | 16.4 us                                                | 19.4 us: 1.18x slower                                                 |
| tomli_loads          | 1.71 sec                                               | 2.07 sec: 1.22x slower                                                |
| xml_etree_process    | 46.5 ms                                                | 59.8 ms: 1.29x slower                                                 |
| pickle_pure_python   | 281 us                                                 | 365 us: 1.30x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 71.9 ms: 1.34x slower                                                 |
| unpickle_pure_python | 194 us                                                 | 280 us: 1.44x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.2 ms: 1.77x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 15.6 ms: 1.98x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.87x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 13.7 ms: 1.39x slower                                                 |
| django_template | 26.4 ms                                                | 37.9 ms: 1.44x slower                                                 |
| genshi_text     | 17.3 ms                                                | 25.8 ms: 1.49x slower                                                 |
| genshi_xml      | 33.8 ms                                                | 51.6 ms: 1.53x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.46x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 151 us: 2.14x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 352 ms: 1.87x faster                                                  |
| async_tree_io            | 980 ms                                                 | 550 ms: 1.78x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 110 ms: 1.73x faster                                                  |
| async_tree_none          | 388 ms                                                 | 243 ms: 1.60x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 300 ms: 1.58x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 504 ms: 1.29x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.25 sec: 1.28x faster                                                |
| regex_dna                | 174 ms                                                 | 139 ms: 1.26x faster                                                  |
| pylint                   | 277 ms                                                 | 224 ms: 1.23x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 696 us: 1.23x faster                                                  |
| gc_traversal             | 2.36 ms                                                | 2.05 ms: 1.15x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 32.4 us: 1.07x faster                                                 |
| deepcopy                 | 272 us                                                 | 256 us: 1.06x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.03x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 405 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.45 ms: 1.00x faster                                                 |
| json_dumps               | 8.11 ms                                                | 8.12 ms: 1.00x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| docutils                 | 1.73 sec                                               | 1.79 sec: 1.04x slower                                                |
| pathlib                  | 24.5 ms                                                | 26.5 ms: 1.08x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 78.2 ms: 1.08x slower                                                 |
| generators               | 32.3 ms                                                | 35.3 ms: 1.09x slower                                                 |
| pycparser                | 877 ms                                                 | 961 ms: 1.10x slower                                                  |
| crypto_pyaes             | 71.8 ms                                                | 78.9 ms: 1.10x slower                                                 |
| deepcopy_reduce          | 2.33 us                                                | 2.57 us: 1.10x slower                                                 |
| json                     | 3.08 ms                                                | 3.42 ms: 1.11x slower                                                 |
| comprehensions           | 16.9 us                                                | 19.3 us: 1.14x slower                                                 |
| pyflate                  | 427 ms                                                 | 489 ms: 1.15x slower                                                  |
| mdp                      | 1.63 sec                                               | 1.87 sec: 1.15x slower                                                |
| meteor_contest           | 77.7 ms                                                | 89.9 ms: 1.16x slower                                                 |
| json_loads               | 16.4 us                                                | 19.4 us: 1.18x slower                                                 |
| richards_super           | 57.8 ms                                                | 68.3 ms: 1.18x slower                                                 |
| fannkuch                 | 303 ms                                                 | 358 ms: 1.18x slower                                                  |
| dulwich_log              | 35.3 ms                                                | 42.1 ms: 1.19x slower                                                 |
| chaos                    | 65.8 ms                                                | 78.5 ms: 1.19x slower                                                 |
| richards                 | 48.7 ms                                                | 58.8 ms: 1.21x slower                                                 |
| deltablue                | 4.91 ms                                                | 5.96 ms: 1.21x slower                                                 |
| tomli_loads              | 1.71 sec                                               | 2.07 sec: 1.22x slower                                                |
| sympy_integrate          | 13.1 ms                                                | 16.0 ms: 1.22x slower                                                 |
| logging_silent           | 117 ns                                                 | 143 ns: 1.22x slower                                                  |
| nqueens                  | 63.8 ms                                                | 78.7 ms: 1.23x slower                                                 |
| html5lib                 | 42.4 ms                                                | 52.3 ms: 1.24x slower                                                 |
| go                       | 151 ms                                                 | 186 ms: 1.24x slower                                                  |
| scimark_fft              | 224 ms                                                 | 279 ms: 1.24x slower                                                  |
| thrift                   | 572 us                                                 | 716 us: 1.25x slower                                                  |
| coroutines               | 20.7 ms                                                | 26.0 ms: 1.26x slower                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 82.6 ms: 1.26x slower                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.32 ms: 1.26x slower                                                 |
| tornado_http             | 86.7 ms                                                | 110 ms: 1.27x slower                                                  |
| hexiom                   | 6.19 ms                                                | 7.94 ms: 1.28x slower                                                 |
| xml_etree_process        | 46.5 ms                                                | 59.8 ms: 1.29x slower                                                 |
| raytrace                 | 301 ms                                                 | 390 ms: 1.30x slower                                                  |
| pickle_pure_python       | 281 us                                                 | 365 us: 1.30x slower                                                  |
| scimark_sor              | 128 ms                                                 | 167 ms: 1.30x slower                                                  |
| regex_compile            | 95.3 ms                                                | 125 ms: 1.32x slower                                                  |
| 2to3                     | 192 ms                                                 | 254 ms: 1.33x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.74 sec: 1.34x slower                                                |
| pprint_safe_repr         | 641 ms                                                 | 859 ms: 1.34x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 71.9 ms: 1.34x slower                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.97 ms: 1.36x slower                                                 |
| coverage                 | 41.5 ms                                                | 56.8 ms: 1.37x slower                                                 |
| sqlglot_parse            | 1.24 ms                                                | 1.72 ms: 1.38x slower                                                 |
| mako                     | 9.87 ms                                                | 13.7 ms: 1.39x slower                                                 |
| spectral_norm            | 94.8 ms                                                | 134 ms: 1.41x slower                                                  |
| logging_simple           | 4.45 us                                                | 6.34 us: 1.43x slower                                                 |
| sympy_str                | 165 ms                                                 | 236 ms: 1.43x slower                                                  |
| float                    | 69.0 ms                                                | 98.7 ms: 1.43x slower                                                 |
| logging_format           | 4.83 us                                                | 6.92 us: 1.43x slower                                                 |
| django_template          | 26.4 ms                                                | 37.9 ms: 1.44x slower                                                 |
| unpickle_pure_python     | 194 us                                                 | 280 us: 1.44x slower                                                  |
| async_generators         | 231 ms                                                 | 336 ms: 1.45x slower                                                  |
| genshi_text              | 17.3 ms                                                | 25.8 ms: 1.49x slower                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 55.0 ms: 1.49x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 56.7 ms: 1.52x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 51.6 ms: 1.53x slower                                                 |
| sympy_sum                | 92.2 ms                                                | 142 ms: 1.54x slower                                                  |
| bench_thread_pool        | 527 us                                                 | 810 us: 1.54x slower                                                  |
| scimark_lu               | 103 ms                                                 | 158 ms: 1.54x slower                                                  |
| sympy_expand             | 269 ms                                                 | 438 ms: 1.63x slower                                                  |
| nbody                    | 93.0 ms                                                | 159 ms: 1.71x slower                                                  |
| telco                    | 3.49 ms                                                | 5.99 ms: 1.72x slower                                                 |
| python_startup           | 10.9 ms                                                | 19.2 ms: 1.77x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 15.6 ms: 1.98x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.16x slower                                                          |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.17x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 0.77x