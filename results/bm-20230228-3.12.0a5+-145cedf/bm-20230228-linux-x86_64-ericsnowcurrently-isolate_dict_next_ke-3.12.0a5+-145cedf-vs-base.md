
# Results vs. base

- fork: ericsnowcurrently
- ref: isolate_dict_next_ke
- machine: linux-x86_64
- commit hash: 145cedf
- commit date: 2023-02-28
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                              |
| docutils       | 2.56 sec                                                               | 2.55 sec: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 73.9 ms                                                                | 75.1 ms: 1.02x slower                                                             |
| pidigits       | 189 ms                                                                 | 193 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 218 ms                                                                 | 200 ms: 1.09x faster                                                              |
| regex_compile  | 135 ms                                                                 | 134 ms: 1.00x faster                                                              |
| regex_v8       | 21.6 ms                                                                | 21.7 ms: 1.00x slower                                                             |
| regex_effbot   | 3.53 ms                                                                | 3.62 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_process    | 56.3 ms                                                                | 56.0 ms: 1.01x faster                                                             |
| xml_etree_generate   | 81.5 ms                                                                | 81.8 ms: 1.00x slower                                                             |
| json_dumps           | 9.51 ms                                                                | 9.59 ms: 1.01x slower                                                             |
| unpickle_pure_python | 202 us                                                                 | 203 us: 1.01x slower                                                              |
| json_loads           | 23.9 us                                                                | 24.2 us: 1.02x slower                                                             |
| unpickle             | 13.6 us                                                                | 13.8 us: 1.02x slower                                                             |
| pickle               | 9.90 us                                                                | 10.1 us: 1.02x slower                                                             |
| pickle_dict          | 30.7 us                                                                | 31.5 us: 1.03x slower                                                             |
| pickle_list          | 4.02 us                                                                | 4.22 us: 1.05x slower                                                             |
| unpickle_list        | 5.00 us                                                                | 5.29 us: 1.06x slower                                                             |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.98 ms                                                                | 9.07 ms: 1.01x slower                                                             |
| python_startup_no_site | 6.51 ms                                                                | 6.57 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                                | 48.0 ms: 1.02x faster                                                             |
| genshi_text     | 21.8 ms                                                                | 21.6 ms: 1.01x faster                                                             |
| django_template | 33.4 ms                                                                | 33.8 ms: 1.01x slower                                                             |
| mako            | 9.92 ms                                                                | 10.0 ms: 1.01x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_next_ke-3.12.0a5+-145cedf |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna               | 218 ms                                                                 | 200 ms: 1.09x faster                                                              |
| gc_traversal            | 4.18 ms                                                                | 3.84 ms: 1.09x faster                                                             |
| pycparser               | 1.15 sec                                                               | 1.10 sec: 1.04x faster                                                            |
| genshi_xml              | 49.0 ms                                                                | 48.0 ms: 1.02x faster                                                             |
| sqlalchemy_imperative   | 18.4 ms                                                                | 18.0 ms: 1.02x faster                                                             |
| generators              | 31.3 ms                                                                | 30.8 ms: 1.02x faster                                                             |
| sympy_expand            | 468 ms                                                                 | 462 ms: 1.01x faster                                                              |
| scimark_sparse_mat_mult | 4.44 ms                                                                | 4.40 ms: 1.01x faster                                                             |
| genshi_text             | 21.8 ms                                                                | 21.6 ms: 1.01x faster                                                             |
| nqueens                 | 82.5 ms                                                                | 81.8 ms: 1.01x faster                                                             |
| dulwich_log             | 63.5 ms                                                                | 63.1 ms: 1.01x faster                                                             |
| hexiom                  | 6.20 ms                                                                | 6.16 ms: 1.01x faster                                                             |
| xml_etree_process       | 56.3 ms                                                                | 56.0 ms: 1.01x faster                                                             |
| mypy2                   | 336 ms                                                                 | 334 ms: 1.00x faster                                                              |
| scimark_fft             | 313 ms                                                                 | 312 ms: 1.00x faster                                                              |
| regex_compile           | 135 ms                                                                 | 134 ms: 1.00x faster                                                              |
| gunicorn                | 1.09 ms                                                                | 1.09 ms: 1.00x faster                                                             |
| sympy_str               | 288 ms                                                                 | 287 ms: 1.00x faster                                                              |
| docutils                | 2.56 sec                                                               | 2.55 sec: 1.00x faster                                                            |
| sqlglot_normalize       | 104 ms                                                                 | 104 ms: 1.00x faster                                                              |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.00x slower                                                             |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.00x slower                                                              |
| regex_v8                | 21.6 ms                                                                | 21.7 ms: 1.00x slower                                                             |
| xml_etree_generate      | 81.5 ms                                                                | 81.8 ms: 1.00x slower                                                             |
| logging_format          | 6.35 us                                                                | 6.39 us: 1.01x slower                                                             |
| bench_thread_pool       | 794 us                                                                 | 799 us: 1.01x slower                                                              |
| crypto_pyaes            | 73.3 ms                                                                | 73.8 ms: 1.01x slower                                                             |
| json_dumps              | 9.51 ms                                                                | 9.59 ms: 1.01x slower                                                             |
| async_generators        | 419 ms                                                                 | 423 ms: 1.01x slower                                                              |
| unpickle_pure_python    | 202 us                                                                 | 203 us: 1.01x slower                                                              |
| python_startup          | 8.98 ms                                                                | 9.07 ms: 1.01x slower                                                             |
| async_tree_io           | 1.28 sec                                                               | 1.29 sec: 1.01x slower                                                            |
| python_startup_no_site  | 6.51 ms                                                                | 6.57 ms: 1.01x slower                                                             |
| comprehensions          | 24.0 us                                                                | 24.2 us: 1.01x slower                                                             |
| django_template         | 33.4 ms                                                                | 33.8 ms: 1.01x slower                                                             |
| thrift                  | 762 us                                                                 | 770 us: 1.01x slower                                                              |
| mako                    | 9.92 ms                                                                | 10.0 ms: 1.01x slower                                                             |
| fannkuch                | 358 ms                                                                 | 362 ms: 1.01x slower                                                              |
| logging_silent          | 95.0 ns                                                                | 96.0 ns: 1.01x slower                                                             |
| telco                   | 6.29 ms                                                                | 6.36 ms: 1.01x slower                                                             |
| pprint_pformat          | 1.40 sec                                                               | 1.41 sec: 1.01x slower                                                            |
| deepcopy_memo           | 34.6 us                                                                | 35.0 us: 1.01x slower                                                             |
| meteor_contest          | 103 ms                                                                 | 104 ms: 1.01x slower                                                              |
| sqlglot_parse           | 1.43 ms                                                                | 1.45 ms: 1.01x slower                                                             |
| go                      | 137 ms                                                                 | 139 ms: 1.01x slower                                                              |
| json_loads              | 23.9 us                                                                | 24.2 us: 1.02x slower                                                             |
| richards                | 43.5 ms                                                                | 44.2 ms: 1.02x slower                                                             |
| raytrace                | 290 ms                                                                 | 295 ms: 1.02x slower                                                              |
| float                   | 73.9 ms                                                                | 75.1 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                                 | 749 ms: 1.02x slower                                                              |
| pathlib                 | 17.7 ms                                                                | 18.0 ms: 1.02x slower                                                             |
| unpickle                | 13.6 us                                                                | 13.8 us: 1.02x slower                                                             |
| deepcopy                | 331 us                                                                 | 337 us: 1.02x slower                                                              |
| create_gc_cycles        | 1.47 ms                                                                | 1.50 ms: 1.02x slower                                                             |
| pidigits                | 189 ms                                                                 | 193 ms: 1.02x slower                                                              |
| unpack_sequence         | 42.7 ns                                                                | 43.6 ns: 1.02x slower                                                             |
| regex_effbot            | 3.53 ms                                                                | 3.62 ms: 1.02x slower                                                             |
| pickle                  | 9.90 us                                                                | 10.1 us: 1.02x slower                                                             |
| pickle_dict             | 30.7 us                                                                | 31.5 us: 1.03x slower                                                             |
| pickle_list             | 4.02 us                                                                | 4.22 us: 1.05x slower                                                             |
| pyflate                 | 408 ms                                                                 | 429 ms: 1.05x slower                                                              |
| scimark_monte_carlo     | 67.0 ms                                                                | 70.7 ms: 1.06x slower                                                             |
| unpickle_list           | 5.00 us                                                                | 5.29 us: 1.06x slower                                                             |
| mdp                     | 2.42 sec                                                               | 2.65 sec: 1.09x slower                                                            |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (30): coverage, scimark_lu, sqlite_synth, coroutines, xml_etree_parse, chaos, nbody, sympy_integrate, asyncio_tcp, logging_simple, sqlglot_optimize, bench_mp_pool, pickle_pure_python, dask, sqlalchemy_declarative, pprint_safe_repr, async_tree_none, xml_etree_iterparse, deltablue, tornado_http, sympy_sum, deepcopy_reduce, scimark_sor, sqlglot_transpile, spectral_norm, html5lib, chameleon, json, djangocms, async_tree_memoization
