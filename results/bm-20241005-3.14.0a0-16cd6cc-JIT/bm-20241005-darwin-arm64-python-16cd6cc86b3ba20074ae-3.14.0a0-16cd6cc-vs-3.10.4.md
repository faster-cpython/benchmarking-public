# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 0.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 181 ms: 1.06x faster                                                  |
| docutils       | 1.73 sec                                               | 1.60 sec: 1.08x faster                                                |
| html5lib       | 42.4 ms                                                | 34.2 ms: 1.24x faster                                                 |
| tornado_http   | 86.7 ms                                                | 73.8 ms: 1.17x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 201 ms: 1.93x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 251 ms: 1.88x faster                                                  |
| async_tree_io           | 980 ms                                                 | 583 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 461 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.7 ms: 1.48x faster                                                 |
| nbody          | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 76.0 ms: 1.25x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.64 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 176 us: 1.60x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 130 us: 1.49x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.36x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 34.6 ms: 1.34x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.14 ms: 1.32x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 50.1 ms: 1.07x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 70.7 ms: 1.02x faster                                                 |
| unpickle             | 8.80 us                                                | 9.01 us: 1.02x slower                                                 |
| pickle               | 6.97 us                                                | 7.43 us: 1.07x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.97 us: 1.08x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.99 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.2 ms: 1.67x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 15.2 ms: 1.93x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.80x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.39 ms: 1.54x faster                                                 |
| django_template | 26.4 ms                                                | 23.4 ms: 1.13x faster                                                 |
| genshi_text     | 17.3 ms                                                | 17.2 ms: 1.01x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 42.7 ms: 1.26x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.5 us: 3.38x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.10x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.41 ms: 2.04x faster                                                 |
| logging_silent           | 117 ns                                                 | 60.7 ns: 1.93x faster                                                 |
| async_tree_none          | 388 ms                                                 | 201 ms: 1.93x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 251 ms: 1.88x faster                                                  |
| deepcopy                 | 272 us                                                 | 157 us: 1.73x faster                                                  |
| raytrace                 | 301 ms                                                 | 177 ms: 1.71x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.69x faster                                                  |
| async_tree_io            | 980 ms                                                 | 583 ms: 1.68x faster                                                  |
| chaos                    | 65.8 ms                                                | 40.5 ms: 1.62x faster                                                 |
| scimark_lu               | 103 ms                                                 | 64.0 ms: 1.61x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 176 us: 1.60x faster                                                  |
| mako                     | 9.87 ms                                                | 6.39 ms: 1.54x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                 |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 441 ms: 1.50x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 130 us: 1.49x faster                                                  |
| float                    | 69.0 ms                                                | 46.7 ms: 1.48x faster                                                 |
| scimark_sor              | 128 ms                                                 | 87.3 ms: 1.47x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 848 us: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.08 us: 1.45x faster                                                 |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.0 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 461 ms: 1.41x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.05 ms: 1.38x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.3 ms: 1.37x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 47.8 ms: 1.37x faster                                                 |
| thrift                   | 572 us                                                 | 419 us: 1.37x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.36x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 34.6 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 323 ms: 1.32x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.14 ms: 1.32x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.70 ms: 1.32x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.9 us: 1.31x faster                                                 |
| pylint                   | 277 ms                                                 | 214 ms: 1.29x faster                                                  |
| pycparser                | 877 ms                                                 | 679 ms: 1.29x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.01 sec: 1.29x faster                                                |
| pprint_safe_repr         | 641 ms                                                 | 501 ms: 1.28x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.27x faster                                                 |
| generators               | 32.3 ms                                                | 25.4 ms: 1.27x faster                                                 |
| regex_compile            | 95.3 ms                                                | 76.0 ms: 1.25x faster                                                 |
| richards_super           | 57.8 ms                                                | 46.6 ms: 1.24x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                                |
| html5lib                 | 42.4 ms                                                | 34.2 ms: 1.24x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                 |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| tornado_http             | 86.7 ms                                                | 73.8 ms: 1.17x faster                                                 |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 78.9 ms: 1.17x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.99 ms: 1.15x faster                                                 |
| fannkuch                 | 303 ms                                                 | 265 ms: 1.14x faster                                                  |
| django_template          | 26.4 ms                                                | 23.4 ms: 1.13x faster                                                 |
| pathlib                  | 24.5 ms                                                | 22.2 ms: 1.10x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.48 sec: 1.10x faster                                                |
| sympy_str                | 165 ms                                                 | 150 ms: 1.10x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 482 us: 1.09x faster                                                  |
| sympy_expand             | 269 ms                                                 | 246 ms: 1.09x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.60 sec: 1.08x faster                                                |
| nqueens                  | 63.8 ms                                                | 59.0 ms: 1.08x faster                                                 |
| richards                 | 48.7 ms                                                | 45.2 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.88 ms: 1.07x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 50.1 ms: 1.07x faster                                                 |
| 2to3                     | 192 ms                                                 | 181 ms: 1.06x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 12.6 ms: 1.04x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 75.1 ms: 1.04x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 70.7 ms: 1.02x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                 |
| genshi_text              | 17.3 ms                                                | 17.2 ms: 1.01x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 188 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.01 us: 1.02x slower                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 37.8 ms: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.04x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.53 us: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 899 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.0 ms: 1.06x slower                                                 |
| pickle                   | 6.97 us                                                | 7.43 us: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.64 ms: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.97 us: 1.08x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.99 us: 1.11x slower                                                 |
| async_generators         | 231 ms                                                 | 291 ms: 1.26x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 42.7 ms: 1.26x slower                                                 |
| telco                    | 3.49 ms                                                | 4.49 ms: 1.29x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 51.4 ms: 1.37x slower                                                 |
| python_startup           | 10.9 ms                                                | 18.2 ms: 1.67x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 15.2 ms: 1.93x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 76.8 ns: 1.97x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 0.67x