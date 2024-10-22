# Results vs. 3.10.4

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: darwin-arm64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 181 ms: 1.06x faster                                                  |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                |
| html5lib       | 42.4 ms                                                | 33.9 ms: 1.25x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 198 ms: 1.96x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 263 ms: 1.80x faster                                                  |
| async_tree_io           | 980 ms                                                 | 581 ms: 1.69x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 455 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.4 ms: 1.49x faster                                                 |
| nbody          | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 76.1 ms: 1.25x faster                                                 |
| regex_dna      | 174 ms                                                 | 148 ms: 1.18x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 177 us: 1.59x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.48x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 34.3 ms: 1.36x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.10 ms: 1.33x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 49.4 ms: 1.08x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| unpickle             | 8.80 us                                                | 9.03 us: 1.03x slower                                                 |
| pickle               | 6.97 us                                                | 7.36 us: 1.06x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list          | 2.74 us                                                | 3.01 us: 1.10x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.97 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.1 ms: 1.75x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 14.8 ms: 1.87x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.81x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.41 ms: 1.54x faster                                                 |
| django_template | 26.4 ms                                                | 23.0 ms: 1.15x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 42.4 ms: 1.25x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.0 us: 3.40x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.7 us: 2.08x faster                                                 |
| logging_silent           | 117 ns                                                 | 56.4 ns: 2.08x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.42 ms: 2.03x faster                                                 |
| async_tree_none          | 388 ms                                                 | 198 ms: 1.96x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 263 ms: 1.80x faster                                                  |
| deepcopy                 | 272 us                                                 | 155 us: 1.75x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                  |
| async_tree_io            | 980 ms                                                 | 581 ms: 1.69x faster                                                  |
| scimark_lu               | 103 ms                                                 | 64.1 ms: 1.60x faster                                                 |
| chaos                    | 65.8 ms                                                | 41.0 ms: 1.60x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 177 us: 1.59x faster                                                  |
| raytrace                 | 301 ms                                                 | 191 ms: 1.58x faster                                                  |
| mako                     | 9.87 ms                                                | 6.41 ms: 1.54x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 441 ms: 1.49x faster                                                  |
| scimark_sor              | 128 ms                                                 | 85.8 ms: 1.49x faster                                                 |
| float                    | 69.0 ms                                                | 46.4 ms: 1.49x faster                                                 |
| richards_super           | 57.8 ms                                                | 39.0 ms: 1.48x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.48x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 45.1 ms: 1.45x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 855 us: 1.45x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.43x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 455 ms: 1.43x faster                                                  |
| logging_format           | 4.83 us                                                | 3.41 us: 1.41x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.38x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.7 ms: 1.38x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.05 ms: 1.37x faster                                                 |
| richards                 | 48.7 ms                                                | 35.6 ms: 1.37x faster                                                 |
| go                       | 151 ms                                                 | 110 ms: 1.37x faster                                                  |
| thrift                   | 572 us                                                 | 420 us: 1.36x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 34.3 ms: 1.36x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.10 ms: 1.33x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.8 us: 1.33x faster                                                 |
| pyflate                  | 427 ms                                                 | 323 ms: 1.32x faster                                                  |
| pylint                   | 277 ms                                                 | 212 ms: 1.31x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.01 sec: 1.30x faster                                                |
| pycparser                | 877 ms                                                 | 682 ms: 1.29x faster                                                  |
| generators               | 32.3 ms                                                | 25.2 ms: 1.28x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 506 ms: 1.27x faster                                                  |
| regex_compile            | 95.3 ms                                                | 76.1 ms: 1.25x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.96 ms: 1.25x faster                                                 |
| html5lib                 | 42.4 ms                                                | 33.9 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| regex_dna                | 174 ms                                                 | 148 ms: 1.18x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 78.3 ms: 1.18x faster                                                 |
| django_template          | 26.4 ms                                                | 23.0 ms: 1.15x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.99 ms: 1.14x faster                                                 |
| fannkuch                 | 303 ms                                                 | 269 ms: 1.13x faster                                                  |
| nqueens                  | 63.8 ms                                                | 57.1 ms: 1.12x faster                                                 |
| sympy_str                | 165 ms                                                 | 150 ms: 1.10x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                |
| bench_thread_pool        | 527 us                                                 | 480 us: 1.10x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.3 ms: 1.10x faster                                                 |
| sympy_expand             | 269 ms                                                 | 246 ms: 1.09x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.50 sec: 1.09x faster                                                |
| xml_etree_generate       | 53.5 ms                                                | 49.4 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.89 ms: 1.07x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                 |
| 2to3                     | 192 ms                                                 | 181 ms: 1.06x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 12.5 ms: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 187 ms: 1.02x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 76.3 ms: 1.02x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                 |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 37.5 ms: 1.02x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.03 us: 1.03x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.53 us: 1.05x slower                                                 |
| pickle                   | 6.97 us                                                | 7.36 us: 1.06x slower                                                 |
| coverage                 | 41.5 ms                                                | 43.9 ms: 1.06x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.61 ms: 1.06x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| pickle_list              | 2.74 us                                                | 3.01 us: 1.10x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.97 us: 1.10x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.91 ms: 1.23x slower                                                 |
| async_generators         | 231 ms                                                 | 290 ms: 1.25x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 42.4 ms: 1.25x slower                                                 |
| telco                    | 3.49 ms                                                | 4.50 ms: 1.29x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 1.29 ms: 1.50x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 62.2 ms: 1.66x slower                                                 |
| python_startup           | 10.9 ms                                                | 19.1 ms: 1.75x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 14.8 ms: 1.87x slower                                                 |
| unpack_sequence          | 39.0 ns                                                | 75.7 ns: 1.94x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (3): tornado_http, json_loads, xml_etree_iterparse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.43x