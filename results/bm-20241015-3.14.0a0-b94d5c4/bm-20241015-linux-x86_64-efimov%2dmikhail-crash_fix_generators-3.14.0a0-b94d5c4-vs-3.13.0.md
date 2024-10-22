# Results vs. 3.13.0

- fork: efimov-mikhail
- ref: crash_fix_generators
- machine: linux-x86_64
- commit hash: b94d5c4
- commit date: 2024-10-15
- overall geometric mean: 1.00x faster
- HPT reliability: 98.65%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 253 ms: 1.05x faster                                                            |
| docutils       | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                          |
| html5lib       | 64.5 ms                                                | 61.1 ms: 1.06x faster                                                           |
| tornado_http   | 91.5 ms                                                | 90.6 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|--------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp        | 488 ms                                                 | 480 ms: 1.02x faster                                                            |
| asyncio_websockets | 555 ms                                                 | 553 ms: 1.00x faster                                                            |
| asyncio_tcp_ssl    | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| async_generators   | 433 ms                                                 | 440 ms: 1.02x slower                                                            |
| coroutines         | 22.5 ms                                                | 24.0 ms: 1.07x slower                                                           |
| Geometric mean     | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 78.0 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| nbody          | 85.7 ms                                                | 89.4 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.49 ms: 1.11x faster                                                           |
| regex_v8       | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                           |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                            |
| regex_compile  | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                           |
| xml_etree_generate   | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                           |
| unpickle             | 14.9 us                                                | 14.7 us: 1.02x faster                                                           |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| tomli_loads          | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| pickle_list          | 5.01 us                                                | 5.06 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 102 ms                                                 | 104 ms: 1.01x slower                                                            |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                            |
| pickle_pure_python   | 300 us                                                 | 308 us: 1.03x slower                                                            |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                           |
| unpickle_list        | 4.96 us                                                | 5.16 us: 1.04x slower                                                           |
| pickle_dict          | 33.2 us                                                | 35.0 us: 1.06x slower                                                           |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| python_startup_no_site | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                           |
| genshi_xml      | 50.3 ms                                                | 50.0 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.01x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-linux-x86_64-efimov%2dmikhail-crash_fix_generators-3.14.0a0-b94d5c4 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                 | 352 us                                                 | 264 us: 1.34x faster                                                            |
| deepcopy_memo            | 38.0 us                                                | 31.2 us: 1.22x faster                                                           |
| go                       | 142 ms                                                 | 120 ms: 1.18x faster                                                            |
| deepcopy_reduce          | 3.17 us                                                | 2.70 us: 1.17x faster                                                           |
| regex_effbot             | 3.88 ms                                                | 3.49 ms: 1.11x faster                                                           |
| mdp                      | 2.74 sec                                               | 2.49 sec: 1.10x faster                                                          |
| pathlib                  | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult  | 5.03 ms                                                | 4.70 ms: 1.07x faster                                                           |
| unpack_sequence          | 42.4 ns                                                | 40.0 ns: 1.06x faster                                                           |
| telco                    | 8.45 ms                                                | 7.98 ms: 1.06x faster                                                           |
| html5lib                 | 64.5 ms                                                | 61.1 ms: 1.06x faster                                                           |
| richards                 | 48.1 ms                                                | 45.9 ms: 1.05x faster                                                           |
| 2to3                     | 265 ms                                                 | 253 ms: 1.05x faster                                                            |
| richards_super           | 54.4 ms                                                | 52.1 ms: 1.05x faster                                                           |
| generators               | 28.8 ms                                                | 27.8 ms: 1.04x faster                                                           |
| regex_v8                 | 25.3 ms                                                | 24.4 ms: 1.04x faster                                                           |
| regex_dna                | 220 ms                                                 | 212 ms: 1.04x faster                                                            |
| thrift                   | 796 us                                                 | 770 us: 1.03x faster                                                            |
| pprint_safe_repr         | 744 ms                                                 | 720 ms: 1.03x faster                                                            |
| scimark_fft              | 369 ms                                                 | 360 ms: 1.03x faster                                                            |
| pycparser                | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                          |
| logging_simple           | 5.66 us                                                | 5.55 us: 1.02x faster                                                           |
| sympy_str                | 274 ms                                                 | 268 ms: 1.02x faster                                                            |
| meteor_contest           | 108 ms                                                 | 105 ms: 1.02x faster                                                            |
| pprint_pformat           | 1.51 sec                                               | 1.48 sec: 1.02x faster                                                          |
| regex_compile            | 131 ms                                                 | 129 ms: 1.02x faster                                                            |
| xml_etree_process        | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                           |
| django_template          | 34.4 ms                                                | 33.8 ms: 1.02x faster                                                           |
| sqlglot_normalize        | 107 ms                                                 | 105 ms: 1.02x faster                                                            |
| xml_etree_generate       | 87.0 ms                                                | 85.5 ms: 1.02x faster                                                           |
| asyncio_tcp              | 488 ms                                                 | 480 ms: 1.02x faster                                                            |
| sqlglot_optimize         | 53.9 ms                                                | 53.1 ms: 1.02x faster                                                           |
| unpickle                 | 14.9 us                                                | 14.7 us: 1.02x faster                                                           |
| json                     | 5.20 ms                                                | 5.12 ms: 1.01x faster                                                           |
| sympy_sum                | 150 ms                                                 | 148 ms: 1.01x faster                                                            |
| tornado_http             | 91.5 ms                                                | 90.6 ms: 1.01x faster                                                           |
| genshi_xml               | 50.3 ms                                                | 50.0 ms: 1.01x faster                                                           |
| json_loads               | 27.0 us                                                | 26.8 us: 1.01x faster                                                           |
| float                    | 78.5 ms                                                | 78.0 ms: 1.01x faster                                                           |
| pyflate                  | 460 ms                                                 | 457 ms: 1.01x faster                                                            |
| tomli_loads              | 2.11 sec                                               | 2.10 sec: 1.01x faster                                                          |
| asyncio_websockets       | 555 ms                                                 | 553 ms: 1.00x faster                                                            |
| sympy_integrate          | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                           |
| python_startup           | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl          | 1.79 sec                                               | 1.79 sec: 1.00x faster                                                          |
| crypto_pyaes             | 73.0 ms                                                | 73.2 ms: 1.00x slower                                                           |
| bpe_tokeniser            | 4.69 sec                                               | 4.71 sec: 1.00x slower                                                          |
| coverage                 | 83.7 ms                                                | 84.2 ms: 1.01x slower                                                           |
| python_startup_no_site   | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                           |
| sqlite_synth             | 2.85 us                                                | 2.87 us: 1.01x slower                                                           |
| pidigits                 | 186 ms                                                 | 187 ms: 1.01x slower                                                            |
| pickle_list              | 5.01 us                                                | 5.06 us: 1.01x slower                                                           |
| typing_runtime_protocols | 159 us                                                 | 161 us: 1.01x slower                                                            |
| docutils                 | 2.58 sec                                               | 2.62 sec: 1.01x slower                                                          |
| xml_etree_iterparse      | 102 ms                                                 | 104 ms: 1.01x slower                                                            |
| mako                     | 11.1 ms                                                | 11.3 ms: 1.01x slower                                                           |
| unpickle_pure_python     | 213 us                                                 | 217 us: 1.02x slower                                                            |
| async_generators         | 433 ms                                                 | 440 ms: 1.02x slower                                                            |
| sqlglot_transpile        | 1.57 ms                                                | 1.60 ms: 1.02x slower                                                           |
| logging_silent           | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| spectral_norm            | 115 ms                                                 | 117 ms: 1.02x slower                                                            |
| comprehensions           | 16.4 us                                                | 16.7 us: 1.02x slower                                                           |
| scimark_monte_carlo      | 66.3 ms                                                | 67.8 ms: 1.02x slower                                                           |
| raytrace                 | 262 ms                                                 | 268 ms: 1.02x slower                                                            |
| sqlglot_parse            | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                           |
| bench_thread_pool        | 815 us                                                 | 837 us: 1.03x slower                                                            |
| pickle_pure_python       | 300 us                                                 | 308 us: 1.03x slower                                                            |
| dulwich_log              | 63.0 ms                                                | 64.7 ms: 1.03x slower                                                           |
| hexiom                   | 6.13 ms                                                | 6.31 ms: 1.03x slower                                                           |
| pickle                   | 11.6 us                                                | 11.9 us: 1.03x slower                                                           |
| scimark_sor              | 122 ms                                                 | 127 ms: 1.04x slower                                                            |
| deltablue                | 3.15 ms                                                | 3.27 ms: 1.04x slower                                                           |
| unpickle_list            | 4.96 us                                                | 5.16 us: 1.04x slower                                                           |
| chaos                    | 58.4 ms                                                | 60.9 ms: 1.04x slower                                                           |
| nbody                    | 85.7 ms                                                | 89.4 ms: 1.04x slower                                                           |
| fannkuch                 | 381 ms                                                 | 401 ms: 1.05x slower                                                            |
| pickle_dict              | 33.2 us                                                | 35.0 us: 1.06x slower                                                           |
| gc_traversal             | 3.81 ms                                                | 4.02 ms: 1.06x slower                                                           |
| coroutines               | 22.5 ms                                                | 24.0 ms: 1.07x slower                                                           |
| json_dumps               | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| create_gc_cycles         | 1.61 ms                                                | 1.79 ms: 1.11x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.0 ms: 2.33x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (7): sympy_expand, genshi_text, scimark_lu, xml_etree_parse, nqueens, logging_format, pylint
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 98.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x