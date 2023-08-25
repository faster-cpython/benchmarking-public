
# Results vs. 3.11.0

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: d83af14
- commit date: 2023-02-23
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 247 ms: 1.05x faster                                                 |
| chameleon      | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                               |
| html5lib       | 64.5 ms                                                | 61.2 ms: 1.05x faster                                                |
| tornado_http   | 96.3 ms                                                | 94.5 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.7 ms: 1.05x faster                                                |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                 |
| nbody          | 93.1 ms                                                | 95.4 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                |
| regex_compile  | 138 ms                                                 | 132 ms: 1.04x faster                                                 |
| regex_dna      | 204 ms                                                 | 199 ms: 1.02x faster                                                 |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.44 ms: 1.33x faster                                                |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                 |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 98.8 ms: 1.05x faster                                                |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                                |
| pickle_list          | 4.11 us                                                | 4.03 us: 1.02x faster                                                |
| pickle               | 10.1 us                                                | 9.91 us: 1.02x faster                                                |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                |
| xml_etree_process    | 53.9 ms                                                | 55.0 ms: 1.02x slower                                                |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.04x slower                                                |
| xml_etree_generate   | 76.2 ms                                                | 80.0 ms: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.99 ms: 1.05x slower                                                |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                |
| genshi_text     | 21.6 ms                                                | 20.6 ms: 1.05x faster                                                |
| mako            | 10.1 ms                                                | 9.90 ms: 1.02x faster                                                |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.4 ms: 2.50x faster                                                |
| asyncio_tcp             | 922 ms                                                 | 503 ms: 1.83x faster                                                 |
| json_dumps              | 12.6 ms                                                | 9.44 ms: 1.33x faster                                                |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                 |
| deltablue               | 3.67 ms                                                | 3.15 ms: 1.17x faster                                                |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                 |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                 |
| regex_effbot            | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                |
| genshi_xml              | 51.8 ms                                                | 46.5 ms: 1.11x faster                                                |
| richards                | 45.7 ms                                                | 41.2 ms: 1.11x faster                                                |
| logging_silent          | 101 ns                                                 | 91.2 ns: 1.11x faster                                                |
| coroutines              | 25.5 ms                                                | 23.0 ms: 1.11x faster                                                |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                |
| gc_traversal            | 4.02 ms                                                | 3.67 ms: 1.10x faster                                                |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                                 |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                               |
| json                    | 4.94 ms                                                | 4.56 ms: 1.08x faster                                                |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                 |
| fannkuch                | 388 ms                                                 | 365 ms: 1.06x faster                                                 |
| spectral_norm           | 100 ms                                                 | 94.5 ms: 1.06x faster                                                |
| logging_format          | 6.68 us                                                | 6.33 us: 1.06x faster                                                |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                 |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.05x faster                                               |
| raytrace                | 297 ms                                                 | 281 ms: 1.05x faster                                                 |
| html5lib                | 64.5 ms                                                | 61.2 ms: 1.05x faster                                                |
| coverage                | 100 ms                                                 | 95.0 ms: 1.05x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 98.8 ms: 1.05x faster                                                |
| hexiom                  | 6.37 ms                                                | 6.07 ms: 1.05x faster                                                |
| sqlglot_optimize        | 53.1 ms                                                | 50.5 ms: 1.05x faster                                                |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                               |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                 |
| float                   | 77.2 ms                                                | 73.7 ms: 1.05x faster                                                |
| 2to3                    | 259 ms                                                 | 247 ms: 1.05x faster                                                 |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.05x faster                                                 |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.05x faster                                                |
| regex_compile           | 138 ms                                                 | 132 ms: 1.04x faster                                                 |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                               |
| logging_simple          | 6.03 us                                                | 5.79 us: 1.04x faster                                                |
| nqueens                 | 83.4 ms                                                | 80.1 ms: 1.04x faster                                                |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                 |
| bench_thread_pool       | 819 us                                                 | 788 us: 1.04x faster                                                 |
| pprint_safe_repr        | 701 ms                                                 | 676 ms: 1.04x faster                                                 |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                |
| scimark_fft             | 328 ms                                                 | 319 ms: 1.03x faster                                                 |
| crypto_pyaes            | 74.7 ms                                                | 72.5 ms: 1.03x faster                                                |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                 |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                 |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                                |
| pyflate                 | 418 ms                                                 | 408 ms: 1.03x faster                                                 |
| regex_dna               | 204 ms                                                 | 199 ms: 1.02x faster                                                 |
| chaos                   | 69.2 ms                                                | 67.6 ms: 1.02x faster                                                |
| deepcopy                | 342 us                                                 | 334 us: 1.02x faster                                                 |
| telco                   | 6.58 ms                                                | 6.45 ms: 1.02x faster                                                |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.02x faster                                                 |
| pickle_list             | 4.11 us                                                | 4.03 us: 1.02x faster                                                |
| tornado_http            | 96.3 ms                                                | 94.5 ms: 1.02x faster                                                |
| mako                    | 10.1 ms                                                | 9.90 ms: 1.02x faster                                                |
| scimark_monte_carlo     | 68.1 ms                                                | 66.9 ms: 1.02x faster                                                |
| pickle                  | 10.1 us                                                | 9.91 us: 1.02x faster                                                |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                                |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                |
| chameleon               | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.00x faster                                                 |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                                |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.02x slower                                                |
| thrift                  | 756 us                                                 | 768 us: 1.02x slower                                                 |
| xml_etree_process       | 53.9 ms                                                | 55.0 ms: 1.02x slower                                                |
| nbody                   | 93.1 ms                                                | 95.4 ms: 1.02x slower                                                |
| deepcopy_reduce         | 2.94 us                                                | 3.01 us: 1.02x slower                                                |
| unpack_sequence         | 43.1 ns                                                | 44.3 ns: 1.03x slower                                                |
| unpickle_list           | 4.91 us                                                | 5.08 us: 1.04x slower                                                |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.67 ms: 1.04x slower                                                |
| async_tree_memoization  | 627 ms                                                 | 654 ms: 1.04x slower                                                 |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                                |
| xml_etree_generate      | 76.2 ms                                                | 80.0 ms: 1.05x slower                                                |
| python_startup          | 8.52 ms                                                | 8.99 ms: 1.05x slower                                                |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                |
| async_generators        | 368 ms                                                 | 408 ms: 1.11x slower                                                 |
| dask                    | 360 ms                                                 | 500 ms: 1.39x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (8): sqlalchemy_imperative, async_tree_none, djangocms, scimark_lu, bench_mp_pool, async_tree_io, async_tree_cpu_io_mixed, sqlglot_transpile
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
