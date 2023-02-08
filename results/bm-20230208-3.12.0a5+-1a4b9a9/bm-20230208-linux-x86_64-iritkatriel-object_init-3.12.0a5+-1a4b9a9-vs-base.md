
# Results vs. base

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 1a4b9a9
- commit date: 2023-02-08
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 2.53 sec                                                               | 2.56 sec: 1.01x slower                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                       |

Benchmark hidden because not significant (4): 2to3, chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 94.3 ms                                                                | 86.0 ms: 1.10x faster                                              |
| pidigits       | 193 ms                                                                 | 190 ms: 1.02x faster                                               |
| float          | 72.9 ms                                                                | 72.1 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                 | 211 ms: 1.04x faster                                               |
| regex_effbot   | 3.36 ms                                                                | 3.32 ms: 1.01x faster                                              |
| regex_v8       | 21.5 ms                                                                | 21.4 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 9.51 ms                                                                | 9.34 ms: 1.02x faster                                              |
| xml_etree_parse      | 150 ms                                                                 | 149 ms: 1.01x faster                                               |
| pickle_dict          | 30.8 us                                                                | 30.6 us: 1.01x faster                                              |
| unpickle_pure_python | 196 us                                                                 | 197 us: 1.01x slower                                               |
| pickle_pure_python   | 286 us                                                                 | 288 us: 1.01x slower                                               |
| json_loads           | 23.5 us                                                                | 23.7 us: 1.01x slower                                              |
| pickle_list          | 4.04 us                                                                | 4.09 us: 1.01x slower                                              |
| xml_etree_generate   | 80.3 ms                                                                | 81.3 ms: 1.01x slower                                              |
| unpickle             | 12.9 us                                                                | 13.1 us: 1.02x slower                                              |
| pickle               | 9.99 us                                                                | 10.2 us: 1.02x slower                                              |
| unpickle_list        | 4.90 us                                                                | 5.04 us: 1.03x slower                                              |
| xml_etree_iterparse  | 103 ms                                                                 | 108 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.90 ms                                                                | 8.97 ms: 1.01x slower                                              |
| python_startup_no_site | 6.46 ms                                                                | 6.51 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 46.9 ms                                                                | 46.4 ms: 1.01x faster                                              |
| django_template | 32.7 ms                                                                | 32.4 ms: 1.01x faster                                              |
| mako            | 9.62 ms                                                                | 9.65 ms: 1.00x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20230208-linux-x86_64-python-eb49d32b9af0b3b01a55-3.12.0a5+-eb49d32 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody                   | 94.3 ms                                                                | 86.0 ms: 1.10x faster                                              |
| coroutines              | 25.5 ms                                                                | 24.5 ms: 1.04x faster                                              |
| regex_dna               | 219 ms                                                                 | 211 ms: 1.04x faster                                               |
| mdp                     | 2.53 sec                                                               | 2.45 sec: 1.04x faster                                             |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 3.90 ms: 1.03x faster                                              |
| deepcopy_reduce         | 3.01 us                                                                | 2.92 us: 1.03x faster                                              |
| scimark_fft             | 307 ms                                                                 | 298 ms: 1.03x faster                                               |
| raytrace                | 288 ms                                                                 | 281 ms: 1.03x faster                                               |
| chaos                   | 65.8 ms                                                                | 64.1 ms: 1.03x faster                                              |
| async_tree_memoization  | 651 ms                                                                 | 635 ms: 1.03x faster                                               |
| crypto_pyaes            | 73.0 ms                                                                | 71.3 ms: 1.02x faster                                              |
| scimark_monte_carlo     | 66.4 ms                                                                | 65.0 ms: 1.02x faster                                              |
| json_dumps              | 9.51 ms                                                                | 9.34 ms: 1.02x faster                                              |
| async_tree_io           | 1.32 sec                                                               | 1.30 sec: 1.02x faster                                             |
| pidigits                | 193 ms                                                                 | 190 ms: 1.02x faster                                               |
| fannkuch                | 374 ms                                                                 | 369 ms: 1.01x faster                                               |
| pprint_safe_repr        | 689 ms                                                                 | 680 ms: 1.01x faster                                               |
| regex_effbot            | 3.36 ms                                                                | 3.32 ms: 1.01x faster                                              |
| deepcopy_memo           | 34.3 us                                                                | 33.9 us: 1.01x faster                                              |
| unpack_sequence         | 43.2 ns                                                                | 42.6 ns: 1.01x faster                                              |
| deepcopy                | 332 us                                                                 | 328 us: 1.01x faster                                               |
| xml_etree_parse         | 150 ms                                                                 | 149 ms: 1.01x faster                                               |
| richards                | 42.7 ms                                                                | 42.2 ms: 1.01x faster                                              |
| float                   | 72.9 ms                                                                | 72.1 ms: 1.01x faster                                              |
| deltablue               | 3.21 ms                                                                | 3.18 ms: 1.01x faster                                              |
| genshi_xml              | 46.9 ms                                                                | 46.4 ms: 1.01x faster                                              |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                               |
| django_template         | 32.7 ms                                                                | 32.4 ms: 1.01x faster                                              |
| logging_silent          | 93.2 ns                                                                | 92.3 ns: 1.01x faster                                              |
| asyncio_tcp             | 494 ms                                                                 | 490 ms: 1.01x faster                                               |
| sqlglot_optimize        | 51.4 ms                                                                | 51.0 ms: 1.01x faster                                              |
| pathlib                 | 17.9 ms                                                                | 17.8 ms: 1.01x faster                                              |
| pickle_dict             | 30.8 us                                                                | 30.6 us: 1.01x faster                                              |
| regex_v8                | 21.5 ms                                                                | 21.4 ms: 1.01x faster                                              |
| pprint_pformat          | 1.40 sec                                                               | 1.40 sec: 1.00x faster                                             |
| aiohttp                 | 1.01 ms                                                                | 1.00 ms: 1.00x faster                                              |
| sympy_integrate         | 19.8 ms                                                                | 19.8 ms: 1.00x slower                                              |
| mako                    | 9.62 ms                                                                | 9.65 ms: 1.00x slower                                              |
| sympy_expand            | 455 ms                                                                 | 457 ms: 1.00x slower                                               |
| unpickle_pure_python    | 196 us                                                                 | 197 us: 1.01x slower                                               |
| scimark_sor             | 107 ms                                                                 | 108 ms: 1.01x slower                                               |
| pyflate                 | 400 ms                                                                 | 403 ms: 1.01x slower                                               |
| coverage                | 96.6 ms                                                                | 97.3 ms: 1.01x slower                                              |
| create_gc_cycles        | 1.46 ms                                                                | 1.47 ms: 1.01x slower                                              |
| python_startup          | 8.90 ms                                                                | 8.97 ms: 1.01x slower                                              |
| go                      | 134 ms                                                                 | 135 ms: 1.01x slower                                               |
| pickle_pure_python      | 286 us                                                                 | 288 us: 1.01x slower                                               |
| python_startup_no_site  | 6.46 ms                                                                | 6.51 ms: 1.01x slower                                              |
| docutils                | 2.53 sec                                                               | 2.56 sec: 1.01x slower                                             |
| json_loads              | 23.5 us                                                                | 23.7 us: 1.01x slower                                              |
| pickle_list             | 4.04 us                                                                | 4.09 us: 1.01x slower                                              |
| logging_format          | 6.27 us                                                                | 6.34 us: 1.01x slower                                              |
| xml_etree_generate      | 80.3 ms                                                                | 81.3 ms: 1.01x slower                                              |
| logging_simple          | 5.72 us                                                                | 5.79 us: 1.01x slower                                              |
| nqueens                 | 77.7 ms                                                                | 78.8 ms: 1.01x slower                                              |
| generators              | 75.2 ms                                                                | 76.5 ms: 1.02x slower                                              |
| unpickle                | 12.9 us                                                                | 13.1 us: 1.02x slower                                              |
| pickle                  | 9.99 us                                                                | 10.2 us: 1.02x slower                                              |
| thrift                  | 749 us                                                                 | 765 us: 1.02x slower                                               |
| meteor_contest          | 105 ms                                                                 | 107 ms: 1.02x slower                                               |
| unpickle_list           | 4.90 us                                                                | 5.04 us: 1.03x slower                                              |
| gc_traversal            | 3.79 ms                                                                | 3.96 ms: 1.04x slower                                              |
| xml_etree_iterparse     | 103 ms                                                                 | 108 ms: 1.05x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                       |

Benchmark hidden because not significant (29): djangocms, json, async_tree_none, tornado_http, xml_etree_process, scimark_lu, html5lib, sqlalchemy_imperative, genshi_text, sqlglot_parse, async_generators, gunicorn, telco, spectral_norm, async_tree_cpu_io_mixed, sqlglot_transpile, chameleon, 2to3, dulwich_log, bench_thread_pool, bench_mp_pool, mypy2, sympy_str, regex_compile, sqlite_synth, hexiom, sympy_sum, pycparser, sqlalchemy_declarative
