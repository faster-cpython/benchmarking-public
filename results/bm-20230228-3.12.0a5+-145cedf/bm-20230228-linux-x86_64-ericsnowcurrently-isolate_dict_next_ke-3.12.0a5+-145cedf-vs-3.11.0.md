
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_dict_next_ke
- machine: linux-x86_64
- commit hash: 145cedf
- commit date: 2023-02-28
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                             |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                            |
| html5lib       | 64.5 ms                                                | 62.5 ms: 1.03x faster                                                             |
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 75.1 ms: 1.03x faster                                                             |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.62 ms: 1.10x faster                                                             |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                              |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                                              |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.59 ms: 1.31x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.12x faster                                                              |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                              |
| pickle_pure_python   | 306 us                                                 | 290 us: 1.05x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.03x faster                                                              |
| pickle_dict          | 31.1 us                                                | 31.5 us: 1.01x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.22 us: 1.03x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 81.8 ms: 1.07x slower                                                             |
| unpickle_list        | 4.91 us                                                | 5.29 us: 1.08x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.07 ms: 1.06x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.57 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                             |
| mako            | 10.1 ms                                                | 10.0 ms: 1.01x faster                                                             |
| django_template | 32.6 ms                                                | 33.8 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.8 ms: 2.39x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 500 ms: 1.85x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.59 ms: 1.31x faster                                                             |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                              |
| deltablue               | 3.67 ms                                                | 3.25 ms: 1.13x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 203 us: 1.12x faster                                                              |
| regex_effbot            | 3.99 ms                                                | 3.62 ms: 1.10x faster                                                             |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                              |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                                             |
| coroutines              | 25.5 ms                                                | 23.4 ms: 1.09x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                             |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                             |
| json                    | 4.94 ms                                                | 4.58 ms: 1.08x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 48.0 ms: 1.08x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                            |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                                              |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                              |
| deepcopy_memo           | 37.0 us                                                | 35.0 us: 1.06x faster                                                             |
| spectral_norm           | 100 ms                                                 | 94.8 ms: 1.06x faster                                                             |
| pickle_pure_python      | 306 us                                                 | 290 us: 1.05x faster                                                              |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                              |
| coverage                | 100 ms                                                 | 95.0 ms: 1.05x faster                                                             |
| logging_silent          | 101 ns                                                 | 96.0 ns: 1.05x faster                                                             |
| gc_traversal            | 4.02 ms                                                | 3.84 ms: 1.05x faster                                                             |
| logging_format          | 6.68 us                                                | 6.39 us: 1.05x faster                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 51.1 ms: 1.04x faster                                                             |
| telco                   | 6.58 ms                                                | 6.36 ms: 1.04x faster                                                             |
| richards                | 45.7 ms                                                | 44.2 ms: 1.03x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                              |
| hexiom                  | 6.37 ms                                                | 6.16 ms: 1.03x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.03x faster                                                              |
| html5lib                | 64.5 ms                                                | 62.5 ms: 1.03x faster                                                             |
| chaos                   | 69.2 ms                                                | 67.1 ms: 1.03x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                            |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                              |
| logging_simple          | 6.03 us                                                | 5.86 us: 1.03x faster                                                             |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                            |
| float                   | 77.2 ms                                                | 75.1 ms: 1.03x faster                                                             |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                              |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                              |
| bench_thread_pool       | 819 us                                                 | 799 us: 1.03x faster                                                              |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                              |
| pprint_safe_repr        | 701 ms                                                 | 685 ms: 1.02x faster                                                              |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.40 ms: 1.02x faster                                                             |
| regex_dna               | 204 ms                                                 | 200 ms: 1.02x faster                                                              |
| nqueens                 | 83.4 ms                                                | 81.8 ms: 1.02x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                             |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                             |
| deepcopy                | 342 us                                                 | 337 us: 1.01x faster                                                              |
| crypto_pyaes            | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                             |
| tornado_http            | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                             |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                              |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                             |
| sympy_str               | 290 ms                                                 | 287 ms: 1.01x faster                                                              |
| dulwich_log             | 63.7 ms                                                | 63.1 ms: 1.01x faster                                                             |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                             |
| raytrace                | 297 ms                                                 | 295 ms: 1.01x faster                                                              |
| mako                    | 10.1 ms                                                | 10.0 ms: 1.01x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                             |
| mdp                     | 2.62 sec                                               | 2.65 sec: 1.01x slower                                                            |
| unpack_sequence         | 43.1 ns                                                | 43.6 ns: 1.01x slower                                                             |
| pickle_dict             | 31.1 us                                                | 31.5 us: 1.01x slower                                                             |
| sympy_sum               | 167 ms                                                 | 169 ms: 1.01x slower                                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 749 ms: 1.01x slower                                                              |
| thrift                  | 756 us                                                 | 770 us: 1.02x slower                                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                             |
| pyflate                 | 418 ms                                                 | 429 ms: 1.02x slower                                                              |
| pickle_list             | 4.11 us                                                | 4.22 us: 1.03x slower                                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.03x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 650 ms: 1.04x slower                                                              |
| django_template         | 32.6 ms                                                | 33.8 ms: 1.04x slower                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 70.7 ms: 1.04x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                                             |
| python_startup          | 8.52 ms                                                | 9.07 ms: 1.06x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 81.8 ms: 1.07x slower                                                             |
| unpickle_list           | 4.91 us                                                | 5.29 us: 1.08x slower                                                             |
| comprehensions          | 22.4 us                                                | 24.2 us: 1.08x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.57 ms: 1.09x slower                                                             |
| async_generators        | 368 ms                                                 | 423 ms: 1.15x slower                                                              |
| dask                    | 360 ms                                                 | 509 ms: 1.41x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (11): async_tree_io, async_tree_none, bench_mp_pool, genshi_text, scimark_lu, djangocms, nbody, sqlalchemy_declarative, pickle, sqlalchemy_imperative, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
