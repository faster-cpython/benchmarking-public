# Results vs. 3.10.4

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: darwin-arm64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 0.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 180 ms: 1.06x faster                                                  |
| docutils       | 1.73 sec                                               | 1.58 sec: 1.10x faster                                                |
| html5lib       | 42.4 ms                                                | 34.3 ms: 1.23x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 200 ms: 1.94x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.89x faster                                                  |
| async_tree_io           | 980 ms                                                 | 587 ms: 1.67x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 461 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.3 ms: 1.49x faster                                                 |
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 75.7 ms: 1.26x faster                                                 |
| regex_dna      | 174 ms                                                 | 147 ms: 1.18x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.68 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 175 us: 1.61x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 130 us: 1.50x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 34.7 ms: 1.34x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.12 ms: 1.32x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 50.4 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 71.7 ms: 1.01x faster                                                 |
| unpickle             | 8.80 us                                                | 9.02 us: 1.03x slower                                                 |
| pickle               | 6.97 us                                                | 7.41 us: 1.06x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.97 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.2 ms: 1.49x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.3 ms: 1.68x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.58x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.35 ms: 1.55x faster                                                 |
| django_template | 26.4 ms                                                | 23.2 ms: 1.14x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.6 ms: 1.04x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 42.5 ms: 1.26x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.7 us: 3.37x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.3 us: 2.13x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.38 ms: 2.06x faster                                                 |
| async_tree_none          | 388 ms                                                 | 200 ms: 1.94x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.7 ns: 1.93x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.89x faster                                                  |
| deepcopy                 | 272 us                                                 | 156 us: 1.75x faster                                                  |
| raytrace                 | 301 ms                                                 | 176 ms: 1.71x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 241 ms: 1.70x faster                                                  |
| async_tree_io            | 980 ms                                                 | 587 ms: 1.67x faster                                                  |
| chaos                    | 65.8 ms                                                | 40.7 ms: 1.62x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 175 us: 1.61x faster                                                  |
| scimark_lu               | 103 ms                                                 | 64.1 ms: 1.61x faster                                                 |
| mako                     | 9.87 ms                                                | 6.35 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.54x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 130 us: 1.50x faster                                                  |
| float                    | 69.0 ms                                                | 46.3 ms: 1.49x faster                                                 |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                  |
| scimark_sor              | 128 ms                                                 | 87.5 ms: 1.47x faster                                                 |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 849 us: 1.46x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 455 ms: 1.45x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.43x faster                                                 |
| logging_format           | 4.83 us                                                | 3.38 us: 1.43x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 66.8 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 461 ms: 1.41x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 47.7 ms: 1.38x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.05 ms: 1.37x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.4 ms: 1.37x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 34.7 ms: 1.34x faster                                                 |
| thrift                   | 572 us                                                 | 427 us: 1.34x faster                                                  |
| pyflate                  | 427 ms                                                 | 322 ms: 1.33x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.12 ms: 1.32x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.70 ms: 1.32x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.9 us: 1.32x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 998 ms: 1.31x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 491 ms: 1.30x faster                                                  |
| pylint                   | 277 ms                                                 | 214 ms: 1.29x faster                                                  |
| pycparser                | 877 ms                                                 | 678 ms: 1.29x faster                                                  |
| generators               | 32.3 ms                                                | 25.0 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                 |
| regex_compile            | 95.3 ms                                                | 75.7 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.25x faster                                                |
| html5lib                 | 42.4 ms                                                | 34.3 ms: 1.23x faster                                                 |
| richards_super           | 57.8 ms                                                | 46.9 ms: 1.23x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| regex_dna                | 174 ms                                                 | 147 ms: 1.18x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 77.9 ms: 1.18x faster                                                 |
| fannkuch                 | 303 ms                                                 | 260 ms: 1.16x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.97 ms: 1.15x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 462 us: 1.14x faster                                                  |
| django_template          | 26.4 ms                                                | 23.2 ms: 1.14x faster                                                 |
| nqueens                  | 63.8 ms                                                | 57.2 ms: 1.11x faster                                                 |
| pathlib                  | 24.5 ms                                                | 22.0 ms: 1.11x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.48 sec: 1.10x faster                                                |
| sympy_str                | 165 ms                                                 | 150 ms: 1.10x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.58 sec: 1.10x faster                                                |
| sympy_expand             | 269 ms                                                 | 247 ms: 1.09x faster                                                  |
| json                     | 3.08 ms                                                | 2.86 ms: 1.08x faster                                                 |
| richards                 | 48.7 ms                                                | 45.2 ms: 1.08x faster                                                 |
| 2to3                     | 192 ms                                                 | 180 ms: 1.06x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 50.4 ms: 1.06x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 12.6 ms: 1.05x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.6 ms: 1.04x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 75.5 ms: 1.03x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 187 ms: 1.01x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 71.7 ms: 1.01x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 37.7 ms: 1.02x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.02 us: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 899 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 43.8 ms: 1.06x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                                 |
| pickle                   | 6.97 us                                                | 7.41 us: 1.06x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.68 ms: 1.09x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.97 us: 1.10x slower                                                 |
| async_generators         | 231 ms                                                 | 290 ms: 1.25x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 42.5 ms: 1.26x slower                                                 |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 51.0 ms: 1.37x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.2 ms: 1.49x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.3 ms: 1.68x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 75.8 ns: 1.94x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (4): tornado_http, xml_etree_parse, pidigits, json_loads
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 0.70x