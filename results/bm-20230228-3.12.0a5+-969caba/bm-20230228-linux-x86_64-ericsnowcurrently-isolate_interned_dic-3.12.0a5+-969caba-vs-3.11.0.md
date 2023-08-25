
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: 969caba
- commit date: 2023-02-28
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| chameleon      | 6.47 ms                                                | 6.44 ms: 1.00x faster                                                             |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                            |
| html5lib       | 64.5 ms                                                | 62.0 ms: 1.04x faster                                                             |
| tornado_http   | 96.3 ms                                                | 95.3 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.4 ms: 1.05x faster                                                             |
| nbody          | 93.1 ms                                                | 92.4 ms: 1.01x faster                                                             |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.67 ms: 1.09x faster                                                             |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                              |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                             |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.47 ms: 1.33x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.12x faster                                                              |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 99.0 ms: 1.05x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                                              |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.01x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.17 us: 1.01x slower                                                             |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                                             |
| pickle               | 10.1 us                                                | 10.4 us: 1.04x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 56.1 ms: 1.04x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 81.4 ms: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.00 ms: 1.06x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.7 ms: 1.06x faster                                                             |
| mako            | 10.1 ms                                                | 9.93 ms: 1.02x faster                                                             |
| genshi_text     | 21.6 ms                                                | 21.7 ms: 1.01x slower                                                             |
| django_template | 32.6 ms                                                | 33.9 ms: 1.04x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.7 ms: 2.39x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 499 ms: 1.85x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.47 ms: 1.33x faster                                                             |
| mypy2                   | 420 ms                                                 | 335 ms: 1.25x faster                                                              |
| deltablue               | 3.67 ms                                                | 3.25 ms: 1.13x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 203 us: 1.12x faster                                                              |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                                              |
| coroutines              | 25.5 ms                                                | 23.3 ms: 1.09x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.67 ms: 1.09x faster                                                             |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                             |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                             |
| logging_silent          | 101 ns                                                 | 93.8 ns: 1.08x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                              |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                            |
| genshi_xml              | 51.8 ms                                                | 48.7 ms: 1.06x faster                                                             |
| fannkuch                | 388 ms                                                 | 365 ms: 1.06x faster                                                              |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                                            |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                                              |
| json                    | 4.94 ms                                                | 4.68 ms: 1.06x faster                                                             |
| float                   | 77.2 ms                                                | 73.4 ms: 1.05x faster                                                             |
| xml_etree_iterparse     | 104 ms                                                 | 99.0 ms: 1.05x faster                                                             |
| spectral_norm           | 100 ms                                                 | 95.8 ms: 1.04x faster                                                             |
| pickle_pure_python      | 306 us                                                 | 293 us: 1.04x faster                                                              |
| logging_format          | 6.68 us                                                | 6.41 us: 1.04x faster                                                             |
| html5lib                | 64.5 ms                                                | 62.0 ms: 1.04x faster                                                             |
| telco                   | 6.58 ms                                                | 6.34 ms: 1.04x faster                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 51.3 ms: 1.04x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.04x faster                                                            |
| coverage                | 100 ms                                                 | 96.7 ms: 1.03x faster                                                             |
| richards                | 45.7 ms                                                | 44.3 ms: 1.03x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                              |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                            |
| unpack_sequence         | 43.1 ns                                                | 41.9 ns: 1.03x faster                                                             |
| chaos                   | 69.2 ms                                                | 67.2 ms: 1.03x faster                                                             |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                              |
| nqueens                 | 83.4 ms                                                | 81.1 ms: 1.03x faster                                                             |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| bench_thread_pool       | 819 us                                                 | 798 us: 1.03x faster                                                              |
| logging_simple          | 6.03 us                                                | 5.89 us: 1.02x faster                                                             |
| pprint_safe_repr        | 701 ms                                                 | 686 ms: 1.02x faster                                                              |
| scimark_monte_carlo     | 68.1 ms                                                | 66.7 ms: 1.02x faster                                                             |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.25 ms: 1.02x faster                                                             |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                              |
| mako                    | 10.1 ms                                                | 9.93 ms: 1.02x faster                                                             |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.01x faster                                                             |
| pyflate                 | 418 ms                                                 | 413 ms: 1.01x faster                                                              |
| sympy_expand            | 475 ms                                                 | 469 ms: 1.01x faster                                                              |
| raytrace                | 297 ms                                                 | 293 ms: 1.01x faster                                                              |
| go                      | 140 ms                                                 | 138 ms: 1.01x faster                                                              |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                             |
| crypto_pyaes            | 74.7 ms                                                | 73.9 ms: 1.01x faster                                                             |
| tornado_http            | 96.3 ms                                                | 95.3 ms: 1.01x faster                                                             |
| deepcopy                | 342 us                                                 | 339 us: 1.01x faster                                                              |
| nbody                   | 93.1 ms                                                | 92.4 ms: 1.01x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.01x faster                                                             |
| chameleon               | 6.47 ms                                                | 6.44 ms: 1.00x faster                                                             |
| sympy_str               | 290 ms                                                 | 289 ms: 1.00x faster                                                              |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                              |
| dulwich_log             | 63.7 ms                                                | 64.0 ms: 1.01x slower                                                             |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                                              |
| genshi_text             | 21.6 ms                                                | 21.7 ms: 1.01x slower                                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.56 ms: 1.01x slower                                                             |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.01x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.17 us: 1.01x slower                                                             |
| sympy_sum               | 167 ms                                                 | 169 ms: 1.01x slower                                                              |
| sqlalchemy_imperative   | 17.9 ms                                                | 18.2 ms: 1.02x slower                                                             |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.75 ms: 1.03x slower                                                             |
| deepcopy_reduce         | 2.94 us                                                | 3.02 us: 1.03x slower                                                             |
| thrift                  | 756 us                                                 | 781 us: 1.03x slower                                                              |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.04x slower                                                             |
| pickle                  | 10.1 us                                                | 10.4 us: 1.04x slower                                                             |
| django_template         | 32.6 ms                                                | 33.9 ms: 1.04x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 56.1 ms: 1.04x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 659 ms: 1.05x slower                                                              |
| python_startup          | 8.52 ms                                                | 9.00 ms: 1.06x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 81.4 ms: 1.07x slower                                                             |
| comprehensions          | 22.4 us                                                | 24.0 us: 1.07x slower                                                             |
| gc_traversal            | 4.02 ms                                                | 4.31 ms: 1.07x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                             |
| async_generators        | 368 ms                                                 | 418 ms: 1.14x slower                                                              |
| dask                    | 360 ms                                                 | 511 ms: 1.42x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (8): unpickle, async_tree_none, sqlalchemy_declarative, bench_mp_pool, async_tree_io, scimark_lu, async_tree_cpu_io_mixed, djangocms
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
