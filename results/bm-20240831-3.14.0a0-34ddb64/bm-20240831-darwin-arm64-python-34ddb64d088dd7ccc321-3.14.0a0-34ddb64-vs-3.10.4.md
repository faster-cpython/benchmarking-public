# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 0.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.46 sec: 1.18x faster                                                |
| html5lib       | 42.4 ms                                                | 30.0 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 193 ms: 2.02x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.89x faster                                                  |
| async_tree_io           | 980 ms                                                 | 595 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.3 ms: 1.57x faster                                                 |
| float          | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.7 ms: 1.41x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.38 ms: 1.27x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.2 ms: 1.01x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.3 ms: 1.03x slower                                                 |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.8 ms: 1.55x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.9 ms: 1.75x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.65x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.03 ms: 1.40x faster                                                 |
| django_template | 26.4 ms                                                | 19.8 ms: 1.33x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 90.9 us: 3.55x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.18 ms: 2.26x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.7 us: 2.08x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| async_tree_none          | 388 ms                                                 | 193 ms: 2.02x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.9 ns: 1.92x faster                                                 |
| go                       | 151 ms                                                 | 79.0 ms: 1.91x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.89x faster                                                  |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.7 ms: 1.84x faster                                                 |
| comprehensions           | 16.9 us                                                | 9.96 us: 1.70x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 739 us: 1.68x faster                                                  |
| async_tree_io            | 980 ms                                                 | 595 ms: 1.65x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.3 ms: 1.64x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 407 ms: 1.62x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 898 us: 1.61x faster                                                  |
| generators               | 32.3 ms                                                | 20.4 ms: 1.58x faster                                                 |
| nbody                    | 93.0 ms                                                | 59.3 ms: 1.57x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                                  |
| scimark_lu               | 103 ms                                                 | 66.6 ms: 1.54x faster                                                 |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.54x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.06 ms: 1.53x faster                                                 |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.2 ms: 1.52x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.44x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.6 ms: 1.42x faster                                                 |
| logging_format           | 4.83 us                                                | 3.40 us: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.41x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 67.1 ms: 1.41x faster                                                 |
| html5lib                 | 42.4 ms                                                | 30.0 ms: 1.41x faster                                                 |
| regex_compile            | 95.3 ms                                                | 67.7 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 456 ms: 1.40x faster                                                  |
| mako                     | 9.87 ms                                                | 7.03 ms: 1.40x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 930 ms: 1.40x faster                                                  |
| scimark_sor              | 128 ms                                                 | 92.9 ms: 1.38x faster                                                 |
| pycparser                | 877 ms                                                 | 642 ms: 1.37x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| thrift                   | 572 us                                                 | 424 us: 1.35x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.1 ms: 1.33x faster                                                 |
| django_template          | 26.4 ms                                                | 19.8 ms: 1.33x faster                                                 |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.4 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.38 ms: 1.27x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                                 |
| sympy_str                | 165 ms                                                 | 132 ms: 1.26x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.79 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.22x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 437 us: 1.21x faster                                                  |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.2 ms: 1.20x faster                                                 |
| 2to3                     | 192 ms                                                 | 160 ms: 1.19x faster                                                  |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.18x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.46 sec: 1.18x faster                                                |
| fannkuch                 | 303 ms                                                 | 261 ms: 1.16x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.2 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.95 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| pathlib                  | 24.5 ms                                                | 24.2 ms: 1.01x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 53.2 ms: 1.01x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.3 ms: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 896 us: 1.04x slower                                                  |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.9 ms: 1.08x slower                                                 |
| async_generators         | 231 ms                                                 | 281 ms: 1.21x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.6 ms: 1.30x slower                                                 |
| telco                    | 3.49 ms                                                | 4.79 ms: 1.37x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.8 ms: 1.55x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.9 ms: 1.75x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): tornado_http, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 0.56x