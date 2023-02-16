
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                  |
| chameleon      | 6.38 ms                                                | 6.57 ms: 1.03x slower                                 |
| html5lib       | 64.8 ms                                                | 60.1 ms: 1.08x faster                                 |
| tornado_http   | 96.5 ms                                                | 94.6 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 76.8 ms                                                | 72.5 ms: 1.06x faster                                 |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                  |
| nbody          | 90.0 ms                                                | 93.1 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 2.93 ms: 1.18x faster                                 |
| regex_v8       | 22.2 ms                                                | 21.6 ms: 1.03x faster                                 |
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                  |
| regex_dna      | 203 ms                                                 | 204 ms: 1.00x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 25.6 us: 1.22x faster                                 |
| pickle               | 9.90 us                                                | 9.56 us: 1.04x faster                                 |
| json_loads           | 26.1 us                                                | 25.4 us: 1.03x faster                                 |
| xml_etree_parse      | 160 ms                                                 | 157 ms: 1.02x faster                                  |
| pickle_pure_python   | 308 us                                                 | 305 us: 1.01x faster                                  |
| unpickle_pure_python | 227 us                                                 | 229 us: 1.01x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.5 ms: 1.01x slower                                 |
| unpickle_list        | 4.99 us                                                | 5.05 us: 1.01x slower                                 |
| pickle_list          | 4.14 us                                                | 4.26 us: 1.03x slower                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (4): xml_etree_process, json_dumps, xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.25 ms: 1.04x faster                                 |
| python_startup_no_site | 6.04 ms                                                | 6.16 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 9.83 ms                                                | 9.88 ms: 1.00x slower                                 |
| django_template | 32.3 ms                                                | 32.8 ms: 1.01x slower                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                          |

All benchmarks:
===============

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-linux-x86_64-python-main-3.11.0b1-8d32a5c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict            | 31.2 us                                                | 25.6 us: 1.22x faster                                 |
| regex_effbot           | 3.46 ms                                                | 2.93 ms: 1.18x faster                                 |
| html5lib               | 64.8 ms                                                | 60.1 ms: 1.08x faster                                 |
| float                  | 76.8 ms                                                | 72.5 ms: 1.06x faster                                 |
| python_startup         | 8.58 ms                                                | 8.25 ms: 1.04x faster                                 |
| pidigits               | 197 ms                                                 | 190 ms: 1.04x faster                                  |
| pickle                 | 9.90 us                                                | 9.56 us: 1.04x faster                                 |
| go                     | 140 ms                                                 | 136 ms: 1.03x faster                                  |
| sympy_sum              | 166 ms                                                 | 161 ms: 1.03x faster                                  |
| regex_v8               | 22.2 ms                                                | 21.6 ms: 1.03x faster                                 |
| json_loads             | 26.1 us                                                | 25.4 us: 1.03x faster                                 |
| sympy_str              | 291 ms                                                 | 284 ms: 1.03x faster                                  |
| thrift                 | 760 us                                                 | 741 us: 1.02x faster                                  |
| sympy_integrate        | 21.0 ms                                                | 20.5 ms: 1.02x faster                                 |
| scimark_monte_carlo    | 68.0 ms                                                | 66.5 ms: 1.02x faster                                 |
| logging_simple         | 6.02 us                                                | 5.89 us: 1.02x faster                                 |
| xml_etree_parse        | 160 ms                                                 | 157 ms: 1.02x faster                                  |
| tornado_http           | 96.5 ms                                                | 94.6 ms: 1.02x faster                                 |
| crypto_pyaes           | 75.7 ms                                                | 74.3 ms: 1.02x faster                                 |
| pyflate                | 419 ms                                                 | 411 ms: 1.02x faster                                  |
| dulwich_log            | 64.0 ms                                                | 62.8 ms: 1.02x faster                                 |
| sympy_expand           | 475 ms                                                 | 468 ms: 1.02x faster                                  |
| regex_compile          | 136 ms                                                 | 135 ms: 1.01x faster                                  |
| deltablue              | 3.66 ms                                                | 3.61 ms: 1.01x faster                                 |
| 2to3                   | 259 ms                                                 | 256 ms: 1.01x faster                                  |
| pathlib                | 18.1 ms                                                | 17.9 ms: 1.01x faster                                 |
| pickle_pure_python     | 308 us                                                 | 305 us: 1.01x faster                                  |
| hexiom                 | 6.34 ms                                                | 6.29 ms: 1.01x faster                                 |
| spectral_norm          | 98.1 ms                                                | 97.6 ms: 1.01x faster                                 |
| logging_format         | 6.48 us                                                | 6.44 us: 1.01x faster                                 |
| unpack_sequence        | 44.5 ns                                                | 44.3 ns: 1.01x faster                                 |
| regex_dna              | 203 ms                                                 | 204 ms: 1.00x slower                                  |
| mako                   | 9.83 ms                                                | 9.88 ms: 1.00x slower                                 |
| unpickle_pure_python   | 227 us                                                 | 229 us: 1.01x slower                                  |
| xml_etree_generate     | 75.9 ms                                                | 76.5 ms: 1.01x slower                                 |
| json                   | 4.87 ms                                                | 4.91 ms: 1.01x slower                                 |
| raytrace               | 291 ms                                                 | 294 ms: 1.01x slower                                  |
| scimark_lu             | 108 ms                                                 | 109 ms: 1.01x slower                                  |
| nqueens                | 83.8 ms                                                | 84.7 ms: 1.01x slower                                 |
| unpickle_list          | 4.99 us                                                | 5.05 us: 1.01x slower                                 |
| django_template        | 32.3 ms                                                | 32.8 ms: 1.01x slower                                 |
| sqlite_synth           | 2.48 us                                                | 2.53 us: 1.02x slower                                 |
| python_startup_no_site | 6.04 ms                                                | 6.16 ms: 1.02x slower                                 |
| pickle_list            | 4.14 us                                                | 4.26 us: 1.03x slower                                 |
| chameleon              | 6.38 ms                                                | 6.57 ms: 1.03x slower                                 |
| nbody                  | 90.0 ms                                                | 93.1 ms: 1.03x slower                                 |
| telco                  | 6.43 ms                                                | 6.84 ms: 1.06x slower                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (13): scimark_sparse_mat_mult, scimark_sor, xml_etree_process, pycparser, chaos, scimark_fft, json_dumps, fannkuch, meteor_contest, logging_silent, xml_etree_iterparse, richards, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
