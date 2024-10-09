# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.40 sec: 1.24x faster                                                |
| html5lib       | 42.4 ms                                                | 31.9 ms: 1.33x faster                                                 |
| tornado_http   | 86.7 ms                                                | 71.8 ms: 1.21x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 197 ms: 1.97x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 248 ms: 1.91x faster                                                  |
| async_tree_io           | 980 ms                                                 | 585 ms: 1.67x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 65.7 ms: 1.42x faster                                                 |
| float          | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.8 ms: 1.40x faster                                                 |
| regex_dna      | 174 ms                                                 | 148 ms: 1.18x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.4 ms: 1.05x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.55x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 140 us: 1.39x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.20 ms: 1.31x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.51 sec: 1.13x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.1 ms: 1.01x slower                                                 |
| unpickle             | 8.80 us                                                | 9.07 us: 1.03x slower                                                 |
| pickle               | 6.97 us                                                | 7.33 us: 1.05x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 3.00 us: 1.10x slower                                                 |
| unpickle_list        | 2.69 us                                                | 3.00 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.3 ms: 1.50x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.3 ms: 1.68x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.59x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.83 ms: 1.45x faster                                                 |
| django_template | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.6 ms: 1.28x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 29.7 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.8 us: 3.48x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.22 ms: 2.22x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.7 us: 2.07x faster                                                 |
| raytrace                 | 301 ms                                                 | 151 ms: 1.99x faster                                                  |
| async_tree_none          | 388 ms                                                 | 197 ms: 1.97x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 248 ms: 1.91x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.5 ns: 1.90x faster                                                 |
| deepcopy                 | 272 us                                                 | 144 us: 1.89x faster                                                  |
| go                       | 151 ms                                                 | 81.6 ms: 1.85x faster                                                 |
| chaos                    | 65.8 ms                                                | 36.0 ms: 1.83x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 241 ms: 1.70x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 736 us: 1.69x faster                                                  |
| async_tree_io            | 980 ms                                                 | 585 ms: 1.67x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.0 ms: 1.65x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 899 us: 1.61x faster                                                  |
| scimark_lu               | 103 ms                                                 | 65.2 ms: 1.58x faster                                                 |
| generators               | 32.3 ms                                                | 20.6 ms: 1.57x faster                                                 |
| pylint                   | 277 ms                                                 | 178 ms: 1.55x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.55x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.55x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.55x faster                                                  |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.08 ms: 1.52x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.7 ms: 1.50x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.04 us: 1.46x faster                                                 |
| logging_format           | 4.83 us                                                | 3.32 us: 1.46x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 455 ms: 1.45x faster                                                  |
| mako                     | 9.87 ms                                                | 6.83 ms: 1.45x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| nbody                    | 93.0 ms                                                | 65.7 ms: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                 |
| regex_compile            | 95.3 ms                                                | 67.8 ms: 1.40x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 51.3 ms: 1.40x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 458 ms: 1.40x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 936 ms: 1.39x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 140 us: 1.39x faster                                                  |
| unpack_sequence          | 39.0 ns                                                | 28.1 ns: 1.39x faster                                                 |
| pycparser                | 877 ms                                                 | 632 ms: 1.39x faster                                                  |
| thrift                   | 572 us                                                 | 416 us: 1.38x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 70.3 ms: 1.35x faster                                                 |
| scimark_sor              | 128 ms                                                 | 95.5 ms: 1.34x faster                                                 |
| django_template          | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 68.8 ms: 1.34x faster                                                 |
| html5lib                 | 42.4 ms                                                | 31.9 ms: 1.33x faster                                                 |
| pyflate                  | 427 ms                                                 | 325 ms: 1.31x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.20 ms: 1.31x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.4 ms: 1.29x faster                                                 |
| genshi_text              | 17.3 ms                                                | 13.6 ms: 1.28x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.4 ms: 1.27x faster                                                 |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.75 ms: 1.25x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| docutils                 | 1.73 sec                                               | 1.40 sec: 1.24x faster                                                |
| nqueens                  | 63.8 ms                                                | 52.2 ms: 1.22x faster                                                 |
| tornado_http             | 86.7 ms                                                | 71.8 ms: 1.21x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.21x faster                                                 |
| scimark_fft              | 224 ms                                                 | 187 ms: 1.20x faster                                                  |
| sympy_expand             | 269 ms                                                 | 224 ms: 1.20x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 30.8 ms: 1.20x faster                                                 |
| 2to3                     | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| regex_dna                | 174 ms                                                 | 148 ms: 1.18x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 455 us: 1.16x faster                                                  |
| fannkuch                 | 303 ms                                                 | 263 ms: 1.15x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.15x faster                                                  |
| pathlib                  | 24.5 ms                                                | 21.4 ms: 1.14x faster                                                 |
| genshi_xml               | 33.8 ms                                                | 29.7 ms: 1.14x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.14x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.51 sec: 1.13x faster                                                |
| json                     | 3.08 ms                                                | 2.82 ms: 1.09x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.6 ms: 1.09x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.4 ms: 1.05x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                 |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.1 ms: 1.01x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.07 us: 1.03x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.50 us: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 900 us: 1.05x slower                                                  |
| pickle                   | 6.97 us                                                | 7.33 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 43.7 ms: 1.05x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 3.00 us: 1.10x slower                                                 |
| unpickle_list            | 2.69 us                                                | 3.00 us: 1.11x slower                                                 |
| async_generators         | 231 ms                                                 | 274 ms: 1.18x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.6 ms: 1.30x slower                                                 |
| telco                    | 3.49 ms                                                | 4.56 ms: 1.31x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.3 ms: 1.50x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.3 ms: 1.68x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 0.86x