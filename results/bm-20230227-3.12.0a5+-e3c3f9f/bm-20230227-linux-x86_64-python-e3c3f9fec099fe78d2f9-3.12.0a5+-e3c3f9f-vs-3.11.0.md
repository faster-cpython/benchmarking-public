
# Results vs. 3.11.0

- fork: python
- ref: e3c3f9fec099fe78d2f9
- machine: linux-x86_64
- commit hash: e3c3f9f
- commit date: 2023-02-27
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.37 ms: 1.02x faster                                                  |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                 |
| html5lib       | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                  |
| tornado_http   | 96.3 ms                                                | 94.2 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.5 ms: 1.07x faster                                                  |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                   |
| nbody          | 93.1 ms                                                | 96.0 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                  |
| regex_compile  | 138 ms                                                 | 131 ms: 1.05x faster                                                   |
| regex_dna      | 204 ms                                                 | 198 ms: 1.03x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.52 ms: 1.32x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 195 us: 1.17x faster                                                   |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 280 us: 1.09x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 99.8 ms: 1.04x faster                                                  |
| unpickle             | 13.7 us                                                | 13.2 us: 1.03x faster                                                  |
| xml_etree_process    | 53.9 ms                                                | 55.1 ms: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.03x slower                                                  |
| pickle_dict          | 31.1 us                                                | 32.5 us: 1.04x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.33 us: 1.05x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.95 ms: 1.05x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| genshi_text     | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                  |
| mako            | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                  |
| django_template | 32.6 ms                                                | 32.5 ms: 1.00x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230227-linux-x86_64-python-e3c3f9fec099fe78d2f9-3.12.0a5+-e3c3f9f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators             | 73.5 ms                                                | 29.9 ms: 2.45x faster                                                  |
| asyncio_tcp            | 922 ms                                                 | 503 ms: 1.83x faster                                                   |
| json_dumps             | 12.6 ms                                                | 9.52 ms: 1.32x faster                                                  |
| mypy2                  | 420 ms                                                 | 332 ms: 1.27x faster                                                   |
| deltablue              | 3.67 ms                                                | 3.11 ms: 1.18x faster                                                  |
| unpickle_pure_python   | 228 us                                                 | 195 us: 1.17x faster                                                   |
| scimark_sor            | 118 ms                                                 | 104 ms: 1.13x faster                                                   |
| richards               | 45.7 ms                                                | 41.0 ms: 1.12x faster                                                  |
| json_loads             | 26.5 us                                                | 23.9 us: 1.11x faster                                                  |
| genshi_xml             | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| fannkuch               | 388 ms                                                 | 352 ms: 1.10x faster                                                   |
| regex_effbot           | 3.99 ms                                                | 3.63 ms: 1.10x faster                                                  |
| logging_silent         | 101 ns                                                 | 92.2 ns: 1.10x faster                                                  |
| gunicorn               | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                  |
| aiohttp                | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                  |
| json                   | 4.94 ms                                                | 4.53 ms: 1.09x faster                                                  |
| pickle_pure_python     | 306 us                                                 | 280 us: 1.09x faster                                                   |
| pycparser              | 1.18 sec                                               | 1.09 sec: 1.09x faster                                                 |
| coroutines             | 25.5 ms                                                | 23.7 ms: 1.08x faster                                                  |
| deepcopy_memo          | 37.0 us                                                | 34.6 us: 1.07x faster                                                  |
| float                  | 77.2 ms                                                | 72.5 ms: 1.07x faster                                                  |
| spectral_norm          | 100 ms                                                 | 94.0 ms: 1.06x faster                                                  |
| nqueens                | 83.4 ms                                                | 78.4 ms: 1.06x faster                                                  |
| hexiom                 | 6.37 ms                                                | 6.00 ms: 1.06x faster                                                  |
| raytrace               | 297 ms                                                 | 280 ms: 1.06x faster                                                   |
| xml_etree_parse        | 158 ms                                                 | 150 ms: 1.06x faster                                                   |
| go                     | 140 ms                                                 | 132 ms: 1.06x faster                                                   |
| html5lib               | 64.5 ms                                                | 61.3 ms: 1.05x faster                                                  |
| regex_compile          | 138 ms                                                 | 131 ms: 1.05x faster                                                   |
| scimark_fft            | 328 ms                                                 | 313 ms: 1.05x faster                                                   |
| logging_format         | 6.68 us                                                | 6.38 us: 1.05x faster                                                  |
| 2to3                   | 259 ms                                                 | 247 ms: 1.05x faster                                                   |
| pprint_pformat         | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| sqlglot_optimize       | 53.1 ms                                                | 50.8 ms: 1.04x faster                                                  |
| sympy_expand           | 475 ms                                                 | 455 ms: 1.04x faster                                                   |
| bench_thread_pool      | 819 us                                                 | 786 us: 1.04x faster                                                   |
| logging_simple         | 6.03 us                                                | 5.79 us: 1.04x faster                                                  |
| xml_etree_iterparse    | 104 ms                                                 | 99.8 ms: 1.04x faster                                                  |
| sqlglot_normalize      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| coverage               | 100 ms                                                 | 96.5 ms: 1.04x faster                                                  |
| crypto_pyaes           | 74.7 ms                                                | 72.1 ms: 1.04x faster                                                  |
| meteor_contest         | 107 ms                                                 | 103 ms: 1.03x faster                                                   |
| sympy_str              | 290 ms                                                 | 281 ms: 1.03x faster                                                   |
| pyflate                | 418 ms                                                 | 405 ms: 1.03x faster                                                   |
| unpickle               | 13.7 us                                                | 13.2 us: 1.03x faster                                                  |
| genshi_text            | 21.6 ms                                                | 20.9 ms: 1.03x faster                                                  |
| pprint_safe_repr       | 701 ms                                                 | 680 ms: 1.03x faster                                                   |
| regex_dna              | 204 ms                                                 | 198 ms: 1.03x faster                                                   |
| docutils               | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                 |
| deepcopy               | 342 us                                                 | 333 us: 1.03x faster                                                   |
| pidigits               | 198 ms                                                 | 193 ms: 1.03x faster                                                   |
| pathlib                | 18.2 ms                                                | 17.8 ms: 1.03x faster                                                  |
| tornado_http           | 96.3 ms                                                | 94.2 ms: 1.02x faster                                                  |
| sympy_integrate        | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                  |
| unpack_sequence        | 43.1 ns                                                | 42.2 ns: 1.02x faster                                                  |
| regex_v8               | 22.0 ms                                                | 21.7 ms: 1.02x faster                                                  |
| sqlalchemy_declarative | 138 ms                                                 | 136 ms: 1.02x faster                                                   |
| chameleon              | 6.47 ms                                                | 6.37 ms: 1.02x faster                                                  |
| chaos                  | 69.2 ms                                                | 68.2 ms: 1.01x faster                                                  |
| create_gc_cycles       | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                  |
| scimark_lu             | 110 ms                                                 | 108 ms: 1.01x faster                                                   |
| sympy_sum              | 167 ms                                                 | 165 ms: 1.01x faster                                                   |
| mako                   | 10.1 ms                                                | 9.99 ms: 1.01x faster                                                  |
| telco                  | 6.58 ms                                                | 6.53 ms: 1.01x faster                                                  |
| dulwich_log            | 63.7 ms                                                | 63.3 ms: 1.01x faster                                                  |
| django_template        | 32.6 ms                                                | 32.5 ms: 1.00x faster                                                  |
| thrift                 | 756 us                                                 | 761 us: 1.01x slower                                                   |
| sqlglot_parse          | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                  |
| xml_etree_process      | 53.9 ms                                                | 55.1 ms: 1.02x slower                                                  |
| pickle                 | 10.1 us                                                | 10.4 us: 1.03x slower                                                  |
| deepcopy_reduce        | 2.94 us                                                | 3.02 us: 1.03x slower                                                  |
| mdp                    | 2.62 sec                                               | 2.69 sec: 1.03x slower                                                 |
| nbody                  | 93.1 ms                                                | 96.0 ms: 1.03x slower                                                  |
| async_tree_memoization | 627 ms                                                 | 649 ms: 1.03x slower                                                   |
| unpickle_list          | 4.91 us                                                | 5.08 us: 1.03x slower                                                  |
| pickle_dict            | 31.1 us                                                | 32.5 us: 1.04x slower                                                  |
| sqlite_synth           | 2.52 us                                                | 2.64 us: 1.05x slower                                                  |
| python_startup         | 8.52 ms                                                | 8.95 ms: 1.05x slower                                                  |
| pickle_list            | 4.11 us                                                | 4.33 us: 1.05x slower                                                  |
| xml_etree_generate     | 76.2 ms                                                | 80.6 ms: 1.06x slower                                                  |
| gc_traversal           | 4.02 ms                                                | 4.30 ms: 1.07x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                  |
| async_generators       | 368 ms                                                 | 409 ms: 1.11x slower                                                   |
| dask                   | 360 ms                                                 | 498 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (9): djangocms, async_tree_none, scimark_sparse_mat_mult, bench_mp_pool, sqlglot_transpile, async_tree_io, scimark_monte_carlo, sqlalchemy_imperative, async_tree_cpu_io_mixed
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
