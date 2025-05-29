# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.489x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.39x faster                                                   |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                 |
| html5lib       | 88.9 ms                                                | 59.1 ms: 1.50x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                                   |
| async_tree_none         | 728 ms                                                 | 251 ms: 2.91x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 308 ms: 2.82x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 482 ms: 2.11x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.68x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.6 ms: 1.73x faster                                                  |
| nbody          | 154 ms                                                 | 89.3 ms: 1.72x faster                                                  |
| pidigits       | 191 ms                                                 | 202 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.41x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                                   |
| regex_dna      | 227 ms                                                 | 194 ms: 1.17x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                  |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.66x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 312 us: 1.55x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                  |
| json_dumps           | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                  |
| unpickle_list        | 5.20 us                                                | 4.46 us: 1.17x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                   |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.03x faster                                                   |
| unpickle             | 14.4 us                                                | 14.0 us: 1.02x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| pickle_dict          | 29.6 us                                                | 35.1 us: 1.18x slower                                                  |
| pickle               | 10.7 us                                                | 13.6 us: 1.27x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.3 ms: 1.59x faster                                                  |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                  |
| mako            | 16.3 ms                                                | 11.7 ms: 1.39x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 47.8 ms: 1.38x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 146 us: 3.72x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                                   |
| async_tree_none          | 728 ms                                                 | 251 ms: 2.91x faster                                                   |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 308 ms: 2.82x faster                                                   |
| deltablue                | 7.91 ms                                                | 2.98 ms: 2.66x faster                                                  |
| go                       | 240 ms                                                 | 113 ms: 2.13x faster                                                   |
| chaos                    | 115 ms                                                 | 54.6 ms: 2.12x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 482 ms: 2.11x faster                                                   |
| logging_silent           | 190 ns                                                 | 90.3 ns: 2.10x faster                                                  |
| spectral_norm            | 170 ms                                                 | 82.3 ms: 2.06x faster                                                  |
| pylint                   | 551 ms                                                 | 270 ms: 2.04x faster                                                   |
| scimark_sor              | 220 ms                                                 | 109 ms: 2.01x faster                                                   |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                  |
| raytrace                 | 507 ms                                                 | 259 ms: 1.96x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 471 ms: 1.96x faster                                                   |
| richards                 | 79.3 ms                                                | 40.8 ms: 1.94x faster                                                  |
| deepcopy                 | 479 us                                                 | 247 us: 1.94x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 61.8 ms: 1.91x faster                                                  |
| comprehensions           | 28.8 us                                                | 15.5 us: 1.86x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.21 ms: 1.79x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                  |
| hexiom                   | 10.4 ms                                                | 5.94 ms: 1.75x faster                                                  |
| float                    | 117 ms                                                 | 67.6 ms: 1.73x faster                                                  |
| nbody                    | 154 ms                                                 | 89.3 ms: 1.72x faster                                                  |
| pyflate                  | 716 ms                                                 | 420 ms: 1.71x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.51 ms: 1.70x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.50 us: 1.67x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.66x faster                                                 |
| coroutines               | 35.1 ms                                                | 21.8 ms: 1.61x faster                                                  |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                   |
| django_template          | 48.2 ms                                                | 30.3 ms: 1.59x faster                                                  |
| scimark_fft              | 466 ms                                                 | 295 ms: 1.58x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.11 ms: 1.57x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 312 us: 1.55x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.37 us: 1.54x faster                                                  |
| logging_format           | 9.09 us                                                | 5.94 us: 1.53x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                   |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                  |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                                   |
| html5lib                 | 88.9 ms                                                | 59.1 ms: 1.50x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.1 ms: 1.45x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.45x faster                                                 |
| thrift                   | 1.07 ms                                                | 742 us: 1.44x faster                                                   |
| nqueens                  | 106 ms                                                 | 73.9 ms: 1.43x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                 |
| 2to3                     | 348 ms                                                 | 250 ms: 1.39x faster                                                   |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.39x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                   |
| sympy_sum                | 196 ms                                                 | 142 ms: 1.38x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 47.8 ms: 1.38x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 125 ms: 1.37x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.36x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 62.2 ms: 1.35x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.1 ms: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                                  |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                   |
| sympy_str                | 346 ms                                                 | 258 ms: 1.34x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 51.8 ms: 1.33x faster                                                  |
| sympy_expand             | 566 ms                                                 | 441 ms: 1.28x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                                   |
| unpack_sequence          | 60.0 ns                                                | 50.1 ns: 1.20x faster                                                  |
| async_generators         | 444 ms                                                 | 378 ms: 1.17x faster                                                   |
| json_dumps               | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.1 ms: 1.17x faster                                                  |
| unpickle_list            | 5.20 us                                                | 4.46 us: 1.17x faster                                                  |
| regex_dna                | 227 ms                                                 | 194 ms: 1.17x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.65 us: 1.14x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                   |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                  |
| json                     | 5.69 ms                                                | 5.45 ms: 1.04x faster                                                  |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.03x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                                 |
| unpickle                 | 14.4 us                                                | 14.0 us: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 79.8 ms: 1.00x slower                                                  |
| telco                    | 7.27 ms                                                | 7.31 ms: 1.01x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| pidigits                 | 191 ms                                                 | 202 ms: 1.06x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                  |
| pickle_dict              | 29.6 us                                                | 35.1 us: 1.18x slower                                                  |
| pickle                   | 10.7 us                                                | 13.6 us: 1.27x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.01 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.50 ms: 1.54x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 80.0 ms: 3.33x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (11) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-linux-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.489x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: 1.27x