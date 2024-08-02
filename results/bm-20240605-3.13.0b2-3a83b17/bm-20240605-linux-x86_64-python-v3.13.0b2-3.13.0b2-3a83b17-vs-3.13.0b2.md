# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.00x slower
- HPT reliability: 66.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                                                   | 274 ms: 1.02x faster                                                                                 |
| chameleon      | 7.11 ms                                                                                                  | 7.22 ms: 1.02x slower                                                                                |
| docutils       | 2.99 sec                                                                                                 | 2.83 sec: 1.06x faster                                                                               |
| html5lib       | 69.1 ms                                                                                                  | 67.2 ms: 1.03x faster                                                                                |
| tornado_http   | 96.9 ms                                                                                                  | 94.6 ms: 1.02x faster                                                                                |
| Geometric mean | (ref)                                                                                                    | 1.02x faster                                                                                         |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                                                   | 191 ms: 1.02x slower                                                                                 |
| nbody          | 83.5 ms                                                                                                  | 88.3 ms: 1.06x slower                                                                                |
| float          | 73.0 ms                                                                                                  | 78.9 ms: 1.08x slower                                                                                |
| Geometric mean | (ref)                                                                                                    | 1.05x slower                                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| regex_dna      | 230 ms                                                                                                   | 221 ms: 1.04x faster                                                                                 |
| regex_compile  | 138 ms                                                                                                   | 137 ms: 1.01x faster                                                                                 |
| regex_effbot   | 3.69 ms                                                                                                  | 3.67 ms: 1.01x faster                                                                                |
| regex_v8       | 25.2 ms                                                                                                  | 25.1 ms: 1.01x faster                                                                                |
| Geometric mean | (ref)                                                                                                    | 1.01x faster                                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| pickle               | 11.9 us                                                                                                  | 11.5 us: 1.03x faster                                                                                |
| unpickle_pure_python | 222 us                                                                                                   | 218 us: 1.02x faster                                                                                 |
| pickle_list          | 5.08 us                                                                                                  | 5.11 us: 1.00x slower                                                                                |
| unpickle_list        | 5.26 us                                                                                                  | 5.34 us: 1.01x slower                                                                                |
| pickle_pure_python   | 300 us                                                                                                   | 305 us: 1.02x slower                                                                                 |
| json_dumps           | 10.3 ms                                                                                                  | 10.7 ms: 1.04x slower                                                                                |
| xml_etree_process    | 58.5 ms                                                                                                  | 61.2 ms: 1.05x slower                                                                                |
| xml_etree_generate   | 82.9 ms                                                                                                  | 87.4 ms: 1.06x slower                                                                                |
| xml_etree_iterparse  | 102 ms                                                                                                   | 107 ms: 1.06x slower                                                                                 |
| xml_etree_parse      | 149 ms                                                                                                   | 162 ms: 1.09x slower                                                                                 |
| tomli_loads          | 1.95 sec                                                                                                 | 2.12 sec: 1.09x slower                                                                               |
| Geometric mean       | (ref)                                                                                                    | 1.02x slower                                                                                         |

Benchmark hidden because not significant (3): pickle_dict, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.62 ms                                                                                                  | 7.11 ms: 1.07x faster                                                                                |
| python_startup         | 11.3 ms                                                                                                  | 10.8 ms: 1.05x faster                                                                                |
| Geometric mean         | (ref)                                                                                                    | 1.06x faster                                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                                                                  | 51.6 ms: 1.17x faster                                                                                |
| genshi_text     | 25.5 ms                                                                                                  | 23.7 ms: 1.08x faster                                                                                |
| django_template | 36.4 ms                                                                                                  | 34.8 ms: 1.05x faster                                                                                |
| mako            | 9.83 ms                                                                                                  | 11.2 ms: 1.14x slower                                                                                |
| Geometric mean  | (ref)                                                                                                    | 1.03x faster                                                                                         |

All benchmarks:
===============

| Benchmark                | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|--------------------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| genshi_xml               | 60.2 ms                                                                                                  | 51.6 ms: 1.17x faster                                                                                |
| deltablue                | 3.70 ms                                                                                                  | 3.25 ms: 1.14x faster                                                                                |
| generators               | 33.5 ms                                                                                                  | 29.6 ms: 1.13x faster                                                                                |
| pylint                   | 353 ms                                                                                                   | 317 ms: 1.11x faster                                                                                 |
| sympy_sum                | 172 ms                                                                                                   | 156 ms: 1.10x faster                                                                                 |
| sympy_integrate          | 22.5 ms                                                                                                  | 20.5 ms: 1.10x faster                                                                                |
| mypy2                    | 814 ms                                                                                                   | 742 ms: 1.10x faster                                                                                 |
| sympy_expand             | 510 ms                                                                                                   | 473 ms: 1.08x faster                                                                                 |
| genshi_text              | 25.5 ms                                                                                                  | 23.7 ms: 1.08x faster                                                                                |
| python_startup_no_site   | 7.62 ms                                                                                                  | 7.11 ms: 1.07x faster                                                                                |
| sympy_str                | 302 ms                                                                                                   | 282 ms: 1.07x faster                                                                                 |
| nqueens                  | 86.5 ms                                                                                                  | 81.4 ms: 1.06x faster                                                                                |
| hexiom                   | 6.67 ms                                                                                                  | 6.30 ms: 1.06x faster                                                                                |
| aiohttp                  | 1.25 ms                                                                                                  | 1.18 ms: 1.06x faster                                                                                |
| docutils                 | 2.99 sec                                                                                                 | 2.83 sec: 1.06x faster                                                                               |
| gunicorn                 | 1.34 ms                                                                                                  | 1.28 ms: 1.05x faster                                                                                |
| typing_runtime_protocols | 173 us                                                                                                   | 165 us: 1.05x faster                                                                                 |
| raytrace                 | 280 ms                                                                                                   | 267 ms: 1.05x faster                                                                                 |
| scimark_lu               | 127 ms                                                                                                   | 122 ms: 1.05x faster                                                                                 |
| python_startup           | 11.3 ms                                                                                                  | 10.8 ms: 1.05x faster                                                                                |
| async_generators         | 462 ms                                                                                                   | 442 ms: 1.05x faster                                                                                 |
| django_template          | 36.4 ms                                                                                                  | 34.8 ms: 1.05x faster                                                                                |
| go                       | 151 ms                                                                                                   | 145 ms: 1.04x faster                                                                                 |
| djangocms                | 32.8 us                                                                                                  | 31.5 us: 1.04x faster                                                                                |
| bench_thread_pool        | 867 us                                                                                                   | 834 us: 1.04x faster                                                                                 |
| dulwich_log              | 69.7 ms                                                                                                  | 67.2 ms: 1.04x faster                                                                                |
| regex_dna                | 230 ms                                                                                                   | 221 ms: 1.04x faster                                                                                 |
| pickle                   | 11.9 us                                                                                                  | 11.5 us: 1.03x faster                                                                                |
| sqlglot_normalize        | 114 ms                                                                                                   | 110 ms: 1.03x faster                                                                                 |
| flaskblogging            | 9.27 ms                                                                                                  | 9.01 ms: 1.03x faster                                                                                |
| html5lib                 | 69.1 ms                                                                                                  | 67.2 ms: 1.03x faster                                                                                |
| asyncio_tcp              | 522 ms                                                                                                   | 508 ms: 1.03x faster                                                                                 |
| logging_silent           | 108 ns                                                                                                   | 105 ns: 1.03x faster                                                                                 |
| 2to3                     | 281 ms                                                                                                   | 274 ms: 1.02x faster                                                                                 |
| tornado_http             | 96.9 ms                                                                                                  | 94.6 ms: 1.02x faster                                                                                |
| sqlglot_optimize         | 56.8 ms                                                                                                  | 55.5 ms: 1.02x faster                                                                                |
| dask                     | 377 ms                                                                                                   | 369 ms: 1.02x faster                                                                                 |
| deepcopy                 | 375 us                                                                                                   | 367 us: 1.02x faster                                                                                 |
| unpickle_pure_python     | 222 us                                                                                                   | 218 us: 1.02x faster                                                                                 |
| regex_compile            | 138 ms                                                                                                   | 137 ms: 1.01x faster                                                                                 |
| meteor_contest           | 111 ms                                                                                                   | 110 ms: 1.01x faster                                                                                 |
| create_gc_cycles         | 1.83 ms                                                                                                  | 1.82 ms: 1.01x faster                                                                                |
| asyncio_tcp_ssl          | 1.86 sec                                                                                                 | 1.84 sec: 1.01x faster                                                                               |
| pathlib                  | 17.4 ms                                                                                                  | 17.3 ms: 1.01x faster                                                                                |
| comprehensions           | 16.7 us                                                                                                  | 16.6 us: 1.01x faster                                                                                |
| regex_effbot             | 3.69 ms                                                                                                  | 3.67 ms: 1.01x faster                                                                                |
| regex_v8                 | 25.2 ms                                                                                                  | 25.1 ms: 1.01x faster                                                                                |
| scimark_sor              | 128 ms                                                                                                   | 127 ms: 1.00x faster                                                                                 |
| sqlglot_transpile        | 1.63 ms                                                                                                  | 1.63 ms: 1.00x slower                                                                                |
| pickle_list              | 5.08 us                                                                                                  | 5.11 us: 1.00x slower                                                                                |
| logging_simple           | 5.70 us                                                                                                  | 5.74 us: 1.01x slower                                                                                |
| deepcopy_reduce          | 3.30 us                                                                                                  | 3.35 us: 1.01x slower                                                                                |
| unpickle_list            | 5.26 us                                                                                                  | 5.34 us: 1.01x slower                                                                                |
| chameleon                | 7.11 ms                                                                                                  | 7.22 ms: 1.02x slower                                                                                |
| pidigits                 | 188 ms                                                                                                   | 191 ms: 1.02x slower                                                                                 |
| sqlglot_parse            | 1.30 ms                                                                                                  | 1.32 ms: 1.02x slower                                                                                |
| pickle_pure_python       | 300 us                                                                                                   | 305 us: 1.02x slower                                                                                 |
| gc_traversal             | 3.88 ms                                                                                                  | 3.98 ms: 1.02x slower                                                                                |
| logging_format           | 6.30 us                                                                                                  | 6.47 us: 1.03x slower                                                                                |
| coroutines               | 22.6 ms                                                                                                  | 23.2 ms: 1.03x slower                                                                                |
| bpe_tokeniser            | 4.88 sec                                                                                                 | 5.02 sec: 1.03x slower                                                                               |
| telco                    | 8.12 ms                                                                                                  | 8.41 ms: 1.04x slower                                                                                |
| json_dumps               | 10.3 ms                                                                                                  | 10.7 ms: 1.04x slower                                                                                |
| sqlite_synth             | 2.88 us                                                                                                  | 2.99 us: 1.04x slower                                                                                |
| xml_etree_process        | 58.5 ms                                                                                                  | 61.2 ms: 1.05x slower                                                                                |
| chaos                    | 58.5 ms                                                                                                  | 61.3 ms: 1.05x slower                                                                                |
| xml_etree_generate       | 82.9 ms                                                                                                  | 87.4 ms: 1.06x slower                                                                                |
| xml_etree_iterparse      | 102 ms                                                                                                   | 107 ms: 1.06x slower                                                                                 |
| nbody                    | 83.5 ms                                                                                                  | 88.3 ms: 1.06x slower                                                                                |
| pprint_safe_repr         | 715 ms                                                                                                   | 758 ms: 1.06x slower                                                                                 |
| mdp                      | 2.62 sec                                                                                                 | 2.79 sec: 1.06x slower                                                                               |
| deepcopy_memo            | 37.3 us                                                                                                  | 39.7 us: 1.06x slower                                                                                |
| pprint_pformat           | 1.45 sec                                                                                                 | 1.56 sec: 1.07x slower                                                                               |
| float                    | 73.0 ms                                                                                                  | 78.9 ms: 1.08x slower                                                                                |
| xml_etree_parse          | 149 ms                                                                                                   | 162 ms: 1.09x slower                                                                                 |
| tomli_loads              | 1.95 sec                                                                                                 | 2.12 sec: 1.09x slower                                                                               |
| scimark_monte_carlo      | 62.7 ms                                                                                                  | 69.2 ms: 1.10x slower                                                                                |
| pyflate                  | 436 ms                                                                                                   | 484 ms: 1.11x slower                                                                                 |
| fannkuch                 | 358 ms                                                                                                   | 402 ms: 1.12x slower                                                                                 |
| spectral_norm            | 102 ms                                                                                                   | 116 ms: 1.14x slower                                                                                 |
| crypto_pyaes             | 68.0 ms                                                                                                  | 77.5 ms: 1.14x slower                                                                                |
| mako                     | 9.83 ms                                                                                                  | 11.2 ms: 1.14x slower                                                                                |
| scimark_sparse_mat_mult  | 4.48 ms                                                                                                  | 5.27 ms: 1.18x slower                                                                                |
| richards_super           | 48.4 ms                                                                                                  | 57.4 ms: 1.19x slower                                                                                |
| richards                 | 41.7 ms                                                                                                  | 50.9 ms: 1.22x slower                                                                                |
| scimark_fft              | 317 ms                                                                                                   | 392 ms: 1.24x slower                                                                                 |
| Geometric mean           | (ref)                                                                                                    | 1.00x slower                                                                                         |

Benchmark hidden because not significant (17): async_tree_io_tg, pycparser, json, thrift, async_tree_cpu_io_mixed, bench_mp_pool, pickle_dict, asyncio_websockets, unpickle, json_loads, async_tree_none, coverage, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization

# HPT report

- Reliability score: 66.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x