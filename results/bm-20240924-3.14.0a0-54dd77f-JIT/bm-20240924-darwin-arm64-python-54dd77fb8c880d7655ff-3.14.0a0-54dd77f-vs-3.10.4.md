# Results vs. 3.10.4

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: darwin-arm64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.237x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 0.74x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 176 ms: 1.09x faster                                                  |
| docutils       | 1.73 sec                                               | 1.56 sec: 1.11x faster                                                |
| html5lib       | 42.4 ms                                                | 32.3 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 201 ms: 1.93x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 249 ms: 1.90x faster                                                  |
| async_tree_io           | 980 ms                                                 | 592 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 461 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.1 ms: 1.50x faster                                                 |
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 75.6 ms: 1.26x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.49x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 34.3 ms: 1.36x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.17 ms: 1.31x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 51.1 ms: 1.05x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 71.7 ms: 1.01x faster                                                 |
| json_loads           | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| unpickle             | 8.80 us                                                | 9.28 us: 1.06x slower                                                 |
| pickle               | 6.97 us                                                | 7.47 us: 1.07x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.89 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.5 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.9 ms: 1.55x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.8 ms: 1.74x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.64x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                 |
| django_template | 26.4 ms                                                | 22.8 ms: 1.16x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 41.3 ms: 1.22x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.6 us: 3.45x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.0 us: 2.17x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.36 ms: 2.09x faster                                                 |
| async_tree_none          | 388 ms                                                 | 201 ms: 1.93x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 249 ms: 1.90x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.5 ns: 1.87x faster                                                 |
| deepcopy                 | 272 us                                                 | 152 us: 1.79x faster                                                  |
| raytrace                 | 301 ms                                                 | 173 ms: 1.74x faster                                                  |
| async_tree_io            | 980 ms                                                 | 592 ms: 1.65x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.9 ms: 1.65x faster                                                 |
| scimark_lu               | 103 ms                                                 | 63.9 ms: 1.61x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 420 ms: 1.57x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.55x faster                                                 |
| mako                     | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                 |
| go                       | 151 ms                                                 | 100 ms: 1.50x faster                                                  |
| float                    | 69.0 ms                                                | 46.1 ms: 1.50x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.49x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.02 us: 1.47x faster                                                 |
| scimark_sor              | 128 ms                                                 | 87.3 ms: 1.47x faster                                                 |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                 |
| logging_format           | 4.83 us                                                | 3.31 us: 1.46x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 855 us: 1.45x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 66.7 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 461 ms: 1.41x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.04 ms: 1.39x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.0 ms: 1.38x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                |
| scimark_monte_carlo      | 65.6 ms                                                | 48.0 ms: 1.37x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 34.3 ms: 1.36x faster                                                 |
| thrift                   | 572 us                                                 | 424 us: 1.35x faster                                                  |
| pylint                   | 277 ms                                                 | 205 ms: 1.35x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.7 us: 1.33x faster                                                 |
| generators               | 32.3 ms                                                | 24.4 ms: 1.32x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.17 ms: 1.31x faster                                                 |
| html5lib                 | 42.4 ms                                                | 32.3 ms: 1.31x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.73 ms: 1.31x faster                                                 |
| pyflate                  | 427 ms                                                 | 327 ms: 1.31x faster                                                  |
| pycparser                | 877 ms                                                 | 685 ms: 1.28x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 504 ms: 1.27x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.03 sec: 1.26x faster                                                |
| regex_compile            | 95.3 ms                                                | 75.6 ms: 1.26x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.4 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.25x faster                                                |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 75.8 ms: 1.22x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| richards_super           | 57.8 ms                                                | 47.9 ms: 1.21x faster                                                 |
| regex_dna                | 174 ms                                                 | 145 ms: 1.21x faster                                                  |
| django_template          | 26.4 ms                                                | 22.8 ms: 1.16x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.96 ms: 1.16x faster                                                 |
| sympy_str                | 165 ms                                                 | 144 ms: 1.15x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.6 ms: 1.14x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                |
| fannkuch                 | 303 ms                                                 | 269 ms: 1.12x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 470 us: 1.12x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.56 sec: 1.11x faster                                                |
| nqueens                  | 63.8 ms                                                | 57.9 ms: 1.10x faster                                                 |
| 2to3                     | 192 ms                                                 | 176 ms: 1.09x faster                                                  |
| sympy_expand             | 269 ms                                                 | 248 ms: 1.09x faster                                                  |
| json                     | 3.08 ms                                                | 2.90 ms: 1.06x faster                                                 |
| richards                 | 48.7 ms                                                | 45.9 ms: 1.06x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 180 ms: 1.06x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 51.1 ms: 1.05x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 35.3 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 74.9 ms: 1.04x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.8 ms: 1.03x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 71.7 ms: 1.01x faster                                                 |
| json_loads               | 16.4 us                                                | 16.8 us: 1.02x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 905 us: 1.05x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.28 us: 1.06x slower                                                 |
| coverage                 | 41.5 ms                                                | 44.4 ms: 1.07x slower                                                 |
| pickle                   | 6.97 us                                                | 7.47 us: 1.07x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.89 us: 1.07x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.58 us: 1.08x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.98 us: 1.09x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.5 us: 1.09x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 41.3 ms: 1.22x slower                                                 |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                                  |
| telco                    | 3.49 ms                                                | 4.78 ms: 1.37x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 51.6 ms: 1.38x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.9 ms: 1.55x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.8 ms: 1.74x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 76.0 ns: 1.95x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (4): tornado_http, asyncio_websockets, pidigits, regex_effbot
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.237x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 0.74x