# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: test_perf_jit
- machine: linux-x86_64
- commit hash: 1973514
- commit date: 2024-05-10
- overall geometric mean: 1.03x slower
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 270 ms: 1.01x faster                                                     |
| chameleon      | 7.22 ms                                                    | 6.94 ms: 1.04x faster                                                    |
| docutils       | 2.83 sec                                                   | 2.81 sec: 1.01x faster                                                   |
| html5lib       | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                      | 1.01x faster                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|--------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none    | 378 ms                                                     | 362 ms: 1.04x faster                                                     |
| async_tree_none_tg | 336 ms                                                     | 347 ms: 1.03x slower                                                     |
| async_tree_io_tg   | 936 ms                                                     | 989 ms: 1.06x slower                                                     |
| Geometric mean     | (ref)                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 77.2 ms: 1.02x faster                                                    |
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                     |
| nbody          | 88.3 ms                                                    | 90.1 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                      | 1.00x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 136 ms: 1.01x faster                                                     |
| regex_dna      | 221 ms                                                     | 220 ms: 1.01x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                    |
| regex_v8       | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict          | 34.8 us                                                    | 34.0 us: 1.02x faster                                                    |
| json_dumps           | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                    |
| tomli_loads          | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 61.8 ms: 1.01x slower                                                    |
| unpickle_pure_python | 218 us                                                     | 221 us: 1.01x slower                                                     |
| pickle               | 11.5 us                                                    | 11.6 us: 1.01x slower                                                    |
| xml_etree_generate   | 87.4 ms                                                    | 89.5 ms: 1.02x slower                                                    |
| unpickle_list        | 5.34 us                                                    | 5.48 us: 1.03x slower                                                    |
| unpickle             | 15.1 us                                                    | 16.2 us: 1.07x slower                                                    |
| pickle_list          | 5.11 us                                                    | 5.63 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_loads, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| python_startup_no_site | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                    |
| genshi_xml      | 51.6 ms                                                    | 50.6 ms: 1.02x faster                                                    |
| mako            | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                    |
| django_template | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240510-linux-x86_64-faster%2dcpython-test_perf_jit-3.14.0a0-1973514 |
|--------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                      | 2.79 sec                                                   | 2.58 sec: 1.08x faster                                                   |
| richards                 | 50.9 ms                                                    | 47.8 ms: 1.07x faster                                                    |
| richards_super           | 57.4 ms                                                    | 54.2 ms: 1.06x faster                                                    |
| async_tree_none          | 378 ms                                                     | 362 ms: 1.04x faster                                                     |
| scimark_fft              | 392 ms                                                     | 377 ms: 1.04x faster                                                     |
| chameleon                | 7.22 ms                                                    | 6.94 ms: 1.04x faster                                                    |
| deepcopy_reduce          | 3.35 us                                                    | 3.22 us: 1.04x faster                                                    |
| gc_traversal             | 3.98 ms                                                    | 3.82 ms: 1.04x faster                                                    |
| scimark_lu               | 122 ms                                                     | 117 ms: 1.04x faster                                                     |
| python_startup           | 10.8 ms                                                    | 10.4 ms: 1.03x faster                                                    |
| crypto_pyaes             | 77.5 ms                                                    | 75.2 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 5.12 ms: 1.03x faster                                                    |
| logging_format           | 6.47 us                                                    | 6.30 us: 1.03x faster                                                    |
| genshi_text              | 23.7 ms                                                    | 23.1 ms: 1.03x faster                                                    |
| spectral_norm            | 116 ms                                                     | 114 ms: 1.02x faster                                                     |
| pickle_dict              | 34.8 us                                                    | 34.0 us: 1.02x faster                                                    |
| thrift                   | 823 us                                                     | 805 us: 1.02x faster                                                     |
| float                    | 78.9 ms                                                    | 77.2 ms: 1.02x faster                                                    |
| genshi_xml               | 51.6 ms                                                    | 50.6 ms: 1.02x faster                                                    |
| dulwich_log              | 67.2 ms                                                    | 65.9 ms: 1.02x faster                                                    |
| json_dumps               | 10.7 ms                                                    | 10.5 ms: 1.02x faster                                                    |
| tomli_loads              | 2.12 sec                                                   | 2.08 sec: 1.02x faster                                                   |
| logging_simple           | 5.74 us                                                    | 5.64 us: 1.02x faster                                                    |
| chaos                    | 61.3 ms                                                    | 60.4 ms: 1.02x faster                                                    |
| flaskblogging            | 9.01 ms                                                    | 8.88 ms: 1.02x faster                                                    |
| logging_silent           | 105 ns                                                     | 103 ns: 1.01x faster                                                     |
| 2to3                     | 274 ms                                                     | 270 ms: 1.01x faster                                                     |
| sqlite_synth             | 2.99 us                                                    | 2.95 us: 1.01x faster                                                    |
| deepcopy_memo            | 39.7 us                                                    | 39.3 us: 1.01x faster                                                    |
| pidigits                 | 191 ms                                                     | 189 ms: 1.01x faster                                                     |
| scimark_sor              | 127 ms                                                     | 126 ms: 1.01x faster                                                     |
| sqlglot_parse            | 1.32 ms                                                    | 1.31 ms: 1.01x faster                                                    |
| scimark_monte_carlo      | 69.2 ms                                                    | 68.5 ms: 1.01x faster                                                    |
| regex_compile            | 137 ms                                                     | 136 ms: 1.01x faster                                                     |
| go                       | 145 ms                                                     | 143 ms: 1.01x faster                                                     |
| html5lib                 | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                                    |
| deepcopy                 | 367 us                                                     | 364 us: 1.01x faster                                                     |
| sqlglot_transpile        | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                    |
| regex_dna                | 221 ms                                                     | 220 ms: 1.01x faster                                                     |
| docutils                 | 2.83 sec                                                   | 2.81 sec: 1.01x faster                                                   |
| create_gc_cycles         | 1.82 ms                                                    | 1.80 ms: 1.01x faster                                                    |
| sqlglot_optimize         | 55.5 ms                                                    | 55.2 ms: 1.01x faster                                                    |
| asyncio_websockets       | 567 ms                                                     | 564 ms: 1.00x faster                                                     |
| asyncio_tcp              | 508 ms                                                     | 506 ms: 1.00x faster                                                     |
| meteor_contest           | 110 ms                                                     | 109 ms: 1.00x faster                                                     |
| sympy_integrate          | 20.5 ms                                                    | 20.4 ms: 1.00x faster                                                    |
| bench_thread_pool        | 834 us                                                     | 831 us: 1.00x faster                                                     |
| python_startup_no_site   | 7.11 ms                                                    | 7.12 ms: 1.00x slower                                                    |
| deltablue                | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                                    |
| raytrace                 | 267 ms                                                     | 268 ms: 1.01x slower                                                     |
| nqueens                  | 81.4 ms                                                    | 81.9 ms: 1.01x slower                                                    |
| mako                     | 11.2 ms                                                    | 11.3 ms: 1.01x slower                                                    |
| pprint_pformat           | 1.56 sec                                                   | 1.57 sec: 1.01x slower                                                   |
| django_template          | 34.8 ms                                                    | 35.1 ms: 1.01x slower                                                    |
| xml_etree_process        | 61.2 ms                                                    | 61.8 ms: 1.01x slower                                                    |
| unpickle_pure_python     | 218 us                                                     | 221 us: 1.01x slower                                                     |
| fannkuch                 | 402 ms                                                     | 407 ms: 1.01x slower                                                     |
| pickle                   | 11.5 us                                                    | 11.6 us: 1.01x slower                                                    |
| typing_runtime_protocols | 165 us                                                     | 167 us: 1.01x slower                                                     |
| pathlib                  | 17.3 ms                                                    | 17.6 ms: 1.02x slower                                                    |
| pprint_safe_repr         | 758 ms                                                     | 771 ms: 1.02x slower                                                     |
| regex_effbot             | 3.67 ms                                                    | 3.73 ms: 1.02x slower                                                    |
| nbody                    | 88.3 ms                                                    | 90.1 ms: 1.02x slower                                                    |
| async_generators         | 442 ms                                                     | 452 ms: 1.02x slower                                                     |
| xml_etree_generate       | 87.4 ms                                                    | 89.5 ms: 1.02x slower                                                    |
| unpickle_list            | 5.34 us                                                    | 5.48 us: 1.03x slower                                                    |
| regex_v8                 | 25.1 ms                                                    | 25.9 ms: 1.03x slower                                                    |
| async_tree_none_tg       | 336 ms                                                     | 347 ms: 1.03x slower                                                     |
| json                     | 5.31 ms                                                    | 5.53 ms: 1.04x slower                                                    |
| async_tree_io_tg         | 936 ms                                                     | 989 ms: 1.06x slower                                                     |
| unpickle                 | 15.1 us                                                    | 16.2 us: 1.07x slower                                                    |
| pickle_list              | 5.11 us                                                    | 5.63 us: 1.10x slower                                                    |
| telco                    | 8.41 ms                                                    | 177 ms: 21.00x slower                                                    |
| Geometric mean           | (ref)                                                      | 1.03x slower                                                             |

Benchmark hidden because not significant (25): xml_etree_iterparse, async_tree_cpu_io_mixed_tg, coverage, async_tree_io, json_loads, dask, bench_mp_pool, comprehensions, tornado_http, hexiom, generators, coroutines, sympy_str, sympy_sum, pylint, pyflate, asyncio_tcp_ssl, pickle_pure_python, xml_etree_parse, sqlglot_normalize, sympy_expand, async_tree_cpu_io_mixed, pycparser, async_tree_memoization_tg, async_tree_memoization
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, djangocms, gunicorn, mypy2

# HPT report

- Reliability score: 99.32% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x