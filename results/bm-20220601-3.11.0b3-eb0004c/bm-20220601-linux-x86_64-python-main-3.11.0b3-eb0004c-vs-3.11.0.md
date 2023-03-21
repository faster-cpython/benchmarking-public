
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                  |
| chameleon      | 6.38 ms                                                | 6.67 ms: 1.05x slower                                 |
| html5lib       | 64.8 ms                                                | 62.6 ms: 1.04x faster                                 |
| tornado_http   | 96.5 ms                                                | 93.8 ms: 1.03x faster                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 76.8 ms                                                | 72.9 ms: 1.05x faster                                 |
| pidigits       | 197 ms                                                 | 194 ms: 1.02x faster                                  |
| nbody          | 90.0 ms                                                | 90.6 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 2.92 ms: 1.18x faster                                 |
| regex_dna      | 203 ms                                                 | 192 ms: 1.06x faster                                  |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                 |
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 25.6 us: 1.22x faster                                 |
| json_loads           | 26.1 us                                                | 24.4 us: 1.07x faster                                 |
| pickle               | 9.90 us                                                | 9.55 us: 1.04x faster                                 |
| xml_etree_parse      | 160 ms                                                 | 156 ms: 1.03x faster                                  |
| pickle_pure_python   | 308 us                                                 | 302 us: 1.02x faster                                  |
| unpickle_list        | 4.99 us                                                | 4.89 us: 1.02x faster                                 |
| unpickle_pure_python | 227 us                                                 | 228 us: 1.00x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 76.3 ms: 1.01x slower                                 |
| json_dumps           | 12.4 ms                                                | 12.5 ms: 1.01x slower                                 |
| pickle_list          | 4.14 us                                                | 4.33 us: 1.04x slower                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (3): xml_etree_process, unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.33 ms: 1.03x faster                                 |
| python_startup_no_site | 6.04 ms                                                | 6.17 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-main-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict            | 31.2 us                                                | 25.6 us: 1.22x faster                                 |
| regex_effbot           | 3.46 ms                                                | 2.92 ms: 1.18x faster                                 |
| pycparser              | 1.19 sec                                               | 1.10 sec: 1.08x faster                                |
| json_loads             | 26.1 us                                                | 24.4 us: 1.07x faster                                 |
| regex_dna              | 203 ms                                                 | 192 ms: 1.06x faster                                  |
| float                  | 76.8 ms                                                | 72.9 ms: 1.05x faster                                 |
| regex_v8               | 22.2 ms                                                | 21.2 ms: 1.05x faster                                 |
| sympy_sum              | 166 ms                                                 | 159 ms: 1.04x faster                                  |
| nqueens                | 83.8 ms                                                | 80.7 ms: 1.04x faster                                 |
| pickle                 | 9.90 us                                                | 9.55 us: 1.04x faster                                 |
| crypto_pyaes           | 75.7 ms                                                | 73.1 ms: 1.04x faster                                 |
| html5lib               | 64.8 ms                                                | 62.6 ms: 1.04x faster                                 |
| fannkuch               | 384 ms                                                 | 372 ms: 1.03x faster                                  |
| scimark_monte_carlo    | 68.0 ms                                                | 66.0 ms: 1.03x faster                                 |
| xml_etree_parse        | 160 ms                                                 | 156 ms: 1.03x faster                                  |
| python_startup         | 8.58 ms                                                | 8.33 ms: 1.03x faster                                 |
| tornado_http           | 96.5 ms                                                | 93.8 ms: 1.03x faster                                 |
| go                     | 140 ms                                                 | 137 ms: 1.03x faster                                  |
| chaos                  | 68.7 ms                                                | 66.9 ms: 1.03x faster                                 |
| scimark_fft            | 325 ms                                                 | 317 ms: 1.03x faster                                  |
| json                   | 4.87 ms                                                | 4.75 ms: 1.03x faster                                 |
| unpack_sequence        | 44.5 ns                                                | 43.4 ns: 1.02x faster                                 |
| sympy_str              | 291 ms                                                 | 284 ms: 1.02x faster                                  |
| sympy_integrate        | 21.0 ms                                                | 20.5 ms: 1.02x faster                                 |
| pickle_pure_python     | 308 us                                                 | 302 us: 1.02x faster                                  |
| unpickle_list          | 4.99 us                                                | 4.89 us: 1.02x faster                                 |
| pidigits               | 197 ms                                                 | 194 ms: 1.02x faster                                  |
| pyflate                | 419 ms                                                 | 411 ms: 1.02x faster                                  |
| sympy_expand           | 475 ms                                                 | 467 ms: 1.02x faster                                  |
| dulwich_log            | 64.0 ms                                                | 63.1 ms: 1.01x faster                                 |
| 2to3                   | 259 ms                                                 | 256 ms: 1.01x faster                                  |
| scimark_lu             | 108 ms                                                 | 107 ms: 1.01x faster                                  |
| logging_simple         | 6.02 us                                                | 5.95 us: 1.01x faster                                 |
| pathlib                | 18.1 ms                                                | 17.9 ms: 1.01x faster                                 |
| deltablue              | 3.66 ms                                                | 3.62 ms: 1.01x faster                                 |
| regex_compile          | 136 ms                                                 | 135 ms: 1.01x faster                                  |
| logging_format         | 6.48 us                                                | 6.44 us: 1.01x faster                                 |
| meteor_contest         | 104 ms                                                 | 104 ms: 1.01x faster                                  |
| spectral_norm          | 98.1 ms                                                | 97.6 ms: 1.00x faster                                 |
| hexiom                 | 6.34 ms                                                | 6.32 ms: 1.00x faster                                 |
| unpickle_pure_python   | 227 us                                                 | 228 us: 1.00x slower                                  |
| xml_etree_generate     | 75.9 ms                                                | 76.3 ms: 1.01x slower                                 |
| nbody                  | 90.0 ms                                                | 90.6 ms: 1.01x slower                                 |
| telco                  | 6.43 ms                                                | 6.49 ms: 1.01x slower                                 |
| json_dumps             | 12.4 ms                                                | 12.5 ms: 1.01x slower                                 |
| django_template        | 32.3 ms                                                | 32.9 ms: 1.02x slower                                 |
| python_startup_no_site | 6.04 ms                                                | 6.17 ms: 1.02x slower                                 |
| logging_silent         | 98.0 ns                                                | 101 ns: 1.04x slower                                  |
| pickle_list            | 4.14 us                                                | 4.33 us: 1.04x slower                                 |
| chameleon              | 6.38 ms                                                | 6.67 ms: 1.05x slower                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                          |

Benchmark hidden because not significant (10): scimark_sparse_mat_mult, mako, thrift, scimark_sor, xml_etree_process, raytrace, unpickle, sqlite_synth, xml_etree_iterparse, richards
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
