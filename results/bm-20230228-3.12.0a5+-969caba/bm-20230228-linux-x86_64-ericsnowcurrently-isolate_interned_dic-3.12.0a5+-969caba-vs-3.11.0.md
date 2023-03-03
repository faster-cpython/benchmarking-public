
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: 969caba
- commit date: 2023-02-28
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| chameleon      | 6.38 ms                                                | 6.44 ms: 1.01x slower                                                             |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                            |
| html5lib       | 64.8 ms                                                | 62.0 ms: 1.05x faster                                                             |
| tornado_http   | 96.5 ms                                                | 95.3 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.4 ms: 1.05x faster                                                             |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                                              |
| nbody          | 90.0 ms                                                | 92.4 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 22.2 ms                                                | 21.7 ms: 1.02x faster                                                             |
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                                              |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                                              |
| regex_effbot   | 3.46 ms                                                | 3.67 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.47 ms: 1.30x faster                                                             |
| unpickle_pure_python | 227 us                                                 | 203 us: 1.12x faster                                                              |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                              |
| json_loads           | 26.1 us                                                | 24.4 us: 1.07x faster                                                             |
| pickle_pure_python   | 308 us                                                 | 293 us: 1.05x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 99.0 ms: 1.05x faster                                                             |
| pickle_list          | 4.14 us                                                | 4.17 us: 1.01x slower                                                             |
| pickle_dict          | 31.2 us                                                | 31.6 us: 1.01x slower                                                             |
| xml_etree_process    | 53.7 ms                                                | 56.1 ms: 1.05x slower                                                             |
| pickle               | 9.90 us                                                | 10.4 us: 1.05x slower                                                             |
| xml_etree_generate   | 75.9 ms                                                | 81.4 ms: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 9.00 ms: 1.05x slower                                                             |
| python_startup_no_site | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.7 ms: 1.06x faster                                                             |
| genshi_text     | 21.5 ms                                                | 21.7 ms: 1.01x slower                                                             |
| mako            | 9.83 ms                                                | 9.93 ms: 1.01x slower                                                             |
| django_template | 32.3 ms                                                | 33.9 ms: 1.05x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                                      |

All benchmarks:
===============

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators             | 73.5 ms                                                | 30.7 ms: 2.40x faster                                                             |
| asyncio_tcp            | 883 ms                                                 | 499 ms: 1.77x faster                                                              |
| json_dumps             | 12.4 ms                                                | 9.47 ms: 1.30x faster                                                             |
| mypy2                  | 420 ms                                                 | 335 ms: 1.25x faster                                                              |
| deltablue              | 3.66 ms                                                | 3.25 ms: 1.13x faster                                                             |
| coroutines             | 26.2 ms                                                | 23.3 ms: 1.12x faster                                                             |
| unpickle_pure_python   | 227 us                                                 | 203 us: 1.12x faster                                                              |
| xml_etree_parse        | 160 ms                                                 | 148 ms: 1.08x faster                                                              |
| scimark_sor            | 115 ms                                                 | 107 ms: 1.07x faster                                                              |
| json_loads             | 26.1 us                                                | 24.4 us: 1.07x faster                                                             |
| pycparser              | 1.19 sec                                               | 1.11 sec: 1.07x faster                                                            |
| mdp                    | 2.63 sec                                               | 2.47 sec: 1.06x faster                                                            |
| unpack_sequence        | 44.5 ns                                                | 41.9 ns: 1.06x faster                                                             |
| genshi_xml             | 51.4 ms                                                | 48.7 ms: 1.06x faster                                                             |
| fannkuch               | 384 ms                                                 | 365 ms: 1.05x faster                                                              |
| pickle_pure_python     | 308 us                                                 | 293 us: 1.05x faster                                                              |
| xml_etree_iterparse    | 104 ms                                                 | 99.0 ms: 1.05x faster                                                             |
| scimark_fft            | 325 ms                                                 | 310 ms: 1.05x faster                                                              |
| float                  | 76.8 ms                                                | 73.4 ms: 1.05x faster                                                             |
| html5lib               | 64.8 ms                                                | 62.0 ms: 1.05x faster                                                             |
| logging_silent         | 98.0 ns                                                | 93.8 ns: 1.05x faster                                                             |
| richards               | 46.1 ms                                                | 44.3 ms: 1.04x faster                                                             |
| json                   | 4.87 ms                                                | 4.68 ms: 1.04x faster                                                             |
| aiohttp                | 1.05 ms                                                | 1.01 ms: 1.04x faster                                                             |
| deepcopy_memo          | 35.8 us                                                | 34.6 us: 1.04x faster                                                             |
| pprint_pformat         | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                            |
| nqueens                | 83.8 ms                                                | 81.1 ms: 1.03x faster                                                             |
| sqlglot_normalize      | 108 ms                                                 | 105 ms: 1.03x faster                                                              |
| pprint_safe_repr       | 706 ms                                                 | 686 ms: 1.03x faster                                                              |
| 2to3                   | 259 ms                                                 | 252 ms: 1.03x faster                                                              |
| sqlglot_optimize       | 52.7 ms                                                | 51.3 ms: 1.03x faster                                                             |
| create_gc_cycles       | 1.52 ms                                                | 1.48 ms: 1.03x faster                                                             |
| coverage               | 99.3 ms                                                | 96.7 ms: 1.03x faster                                                             |
| gunicorn               | 1.12 ms                                                | 1.09 ms: 1.03x faster                                                             |
| regex_v8               | 22.2 ms                                                | 21.7 ms: 1.02x faster                                                             |
| crypto_pyaes           | 75.7 ms                                                | 73.9 ms: 1.02x faster                                                             |
| spectral_norm          | 98.1 ms                                                | 95.8 ms: 1.02x faster                                                             |
| bench_thread_pool      | 817 us                                                 | 798 us: 1.02x faster                                                              |
| logging_simple         | 6.02 us                                                | 5.89 us: 1.02x faster                                                             |
| chaos                  | 68.7 ms                                                | 67.2 ms: 1.02x faster                                                             |
| docutils               | 2.60 sec                                               | 2.55 sec: 1.02x faster                                                            |
| scimark_monte_carlo    | 68.0 ms                                                | 66.7 ms: 1.02x faster                                                             |
| regex_compile          | 136 ms                                                 | 134 ms: 1.02x faster                                                              |
| go                     | 140 ms                                                 | 138 ms: 1.02x faster                                                              |
| pyflate                | 419 ms                                                 | 413 ms: 1.01x faster                                                              |
| hexiom                 | 6.34 ms                                                | 6.25 ms: 1.01x faster                                                             |
| sympy_expand           | 475 ms                                                 | 469 ms: 1.01x faster                                                              |
| telco                  | 6.43 ms                                                | 6.34 ms: 1.01x faster                                                             |
| tornado_http           | 96.5 ms                                                | 95.3 ms: 1.01x faster                                                             |
| pathlib                | 18.1 ms                                                | 17.9 ms: 1.01x faster                                                             |
| sympy_integrate        | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                             |
| logging_format         | 6.48 us                                                | 6.41 us: 1.01x faster                                                             |
| sympy_str              | 291 ms                                                 | 289 ms: 1.01x faster                                                              |
| deepcopy               | 341 us                                                 | 339 us: 1.01x faster                                                              |
| pidigits               | 197 ms                                                 | 198 ms: 1.00x slower                                                              |
| raytrace               | 291 ms                                                 | 293 ms: 1.01x slower                                                              |
| pickle_list            | 4.14 us                                                | 4.17 us: 1.01x slower                                                             |
| genshi_text            | 21.5 ms                                                | 21.7 ms: 1.01x slower                                                             |
| mako                   | 9.83 ms                                                | 9.93 ms: 1.01x slower                                                             |
| chameleon              | 6.38 ms                                                | 6.44 ms: 1.01x slower                                                             |
| regex_dna              | 203 ms                                                 | 205 ms: 1.01x slower                                                              |
| pickle_dict            | 31.2 us                                                | 31.6 us: 1.01x slower                                                             |
| sympy_sum              | 166 ms                                                 | 169 ms: 1.02x slower                                                              |
| scimark_lu             | 108 ms                                                 | 110 ms: 1.02x slower                                                              |
| nbody                  | 90.0 ms                                                | 92.4 ms: 1.03x slower                                                             |
| thrift                 | 760 us                                                 | 781 us: 1.03x slower                                                              |
| xml_etree_process      | 53.7 ms                                                | 56.1 ms: 1.05x slower                                                             |
| django_template        | 32.3 ms                                                | 33.9 ms: 1.05x slower                                                             |
| sqlite_synth           | 2.48 us                                                | 2.60 us: 1.05x slower                                                             |
| python_startup         | 8.58 ms                                                | 9.00 ms: 1.05x slower                                                             |
| pickle                 | 9.90 us                                                | 10.4 us: 1.05x slower                                                             |
| async_tree_memoization | 624 ms                                                 | 659 ms: 1.05x slower                                                              |
| sqlglot_transpile      | 1.65 ms                                                | 1.75 ms: 1.06x slower                                                             |
| regex_effbot           | 3.46 ms                                                | 3.67 ms: 1.06x slower                                                             |
| sqlglot_parse          | 1.36 ms                                                | 1.45 ms: 1.07x slower                                                             |
| xml_etree_generate     | 75.9 ms                                                | 81.4 ms: 1.07x slower                                                             |
| python_startup_no_site | 6.04 ms                                                | 6.53 ms: 1.08x slower                                                             |
| gc_traversal           | 3.82 ms                                                | 4.31 ms: 1.13x slower                                                             |
| async_generators       | 356 ms                                                 | 418 ms: 1.18x slower                                                              |
| dask                   | 365 ms                                                 | 511 ms: 1.40x slower                                                              |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (13): scimark_sparse_mat_mult, async_tree_none, sqlalchemy_declarative, async_tree_io, bench_mp_pool, dulwich_log, deepcopy_reduce, unpickle_list, meteor_contest, djangocms, async_tree_cpu_io_mixed, sqlalchemy_imperative, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-969caba/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba.json: comprehensions
