
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: c4e4b91
- commit date: 2022-02-03
- overall geometric mean: 1.04x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                  |
| chameleon      | 6.38 ms                                                | 6.95 ms: 1.09x slower                                 |
| html5lib       | 64.8 ms                                                | 67.9 ms: 1.05x slower                                 |
| tornado_http   | 96.5 ms                                                | 106 ms: 1.09x slower                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                  |
| float          | 76.8 ms                                                | 77.5 ms: 1.01x slower                                 |
| nbody          | 90.0 ms                                                | 94.7 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.14 ms: 1.10x faster                                 |
| regex_compile  | 136 ms                                                 | 140 ms: 1.03x slower                                  |
| regex_dna      | 203 ms                                                 | 213 ms: 1.05x slower                                  |
| regex_v8       | 22.2 ms                                                | 24.0 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 28.1 us: 1.11x faster                                 |
| xml_etree_parse      | 160 ms                                                 | 153 ms: 1.05x faster                                  |
| json_dumps           | 12.4 ms                                                | 12.2 ms: 1.01x faster                                 |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                  |
| json_loads           | 26.1 us                                                | 26.7 us: 1.02x slower                                 |
| xml_etree_generate   | 75.9 ms                                                | 79.6 ms: 1.05x slower                                 |
| unpickle_list        | 4.99 us                                                | 5.26 us: 1.06x slower                                 |
| xml_etree_process    | 53.7 ms                                                | 57.0 ms: 1.06x slower                                 |
| pickle_list          | 4.14 us                                                | 4.47 us: 1.08x slower                                 |
| pickle_pure_python   | 308 us                                                 | 334 us: 1.08x slower                                  |
| unpickle_pure_python | 227 us                                                 | 249 us: 1.10x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.13 ms: 1.05x faster                                 |
| python_startup_no_site | 6.04 ms                                                | 5.92 ms: 1.02x faster                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 9.83 ms                                                | 10.5 ms: 1.07x slower                                 |
| django_template | 32.3 ms                                                | 35.4 ms: 1.10x slower                                 |
| Geometric mean  | (ref)                                                  | 1.08x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220203-linux-x86_64-python-main-3.11.0a5-c4e4b91 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict             | 31.2 us                                                | 28.1 us: 1.11x faster                                 |
| regex_effbot            | 3.46 ms                                                | 3.14 ms: 1.10x faster                                 |
| python_startup          | 8.58 ms                                                | 8.13 ms: 1.05x faster                                 |
| xml_etree_parse         | 160 ms                                                 | 153 ms: 1.05x faster                                  |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                  |
| logging_simple          | 6.02 us                                                | 5.84 us: 1.03x faster                                 |
| python_startup_no_site  | 6.04 ms                                                | 5.92 ms: 1.02x faster                                 |
| logging_format          | 6.48 us                                                | 6.37 us: 1.02x faster                                 |
| json_dumps              | 12.4 ms                                                | 12.2 ms: 1.01x faster                                 |
| float                   | 76.8 ms                                                | 77.5 ms: 1.01x slower                                 |
| sympy_integrate         | 21.0 ms                                                | 21.3 ms: 1.01x slower                                 |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                  |
| pathlib                 | 18.1 ms                                                | 18.5 ms: 1.02x slower                                 |
| sympy_sum               | 166 ms                                                 | 170 ms: 1.02x slower                                  |
| json_loads              | 26.1 us                                                | 26.7 us: 1.02x slower                                 |
| dulwich_log             | 64.0 ms                                                | 65.7 ms: 1.03x slower                                 |
| regex_compile           | 136 ms                                                 | 140 ms: 1.03x slower                                  |
| 2to3                    | 259 ms                                                 | 267 ms: 1.03x slower                                  |
| unpack_sequence         | 44.5 ns                                                | 46.0 ns: 1.04x slower                                 |
| nqueens                 | 83.8 ms                                                | 87.2 ms: 1.04x slower                                 |
| fannkuch                | 384 ms                                                 | 400 ms: 1.04x slower                                  |
| telco                   | 6.43 ms                                                | 6.70 ms: 1.04x slower                                 |
| sympy_str               | 291 ms                                                 | 304 ms: 1.04x slower                                  |
| regex_dna               | 203 ms                                                 | 213 ms: 1.05x slower                                  |
| html5lib                | 64.8 ms                                                | 67.9 ms: 1.05x slower                                 |
| xml_etree_generate      | 75.9 ms                                                | 79.6 ms: 1.05x slower                                 |
| go                      | 140 ms                                                 | 147 ms: 1.05x slower                                  |
| nbody                   | 90.0 ms                                                | 94.7 ms: 1.05x slower                                 |
| unpickle_list           | 4.99 us                                                | 5.26 us: 1.06x slower                                 |
| sympy_expand            | 475 ms                                                 | 503 ms: 1.06x slower                                  |
| xml_etree_process       | 53.7 ms                                                | 57.0 ms: 1.06x slower                                 |
| spectral_norm           | 98.1 ms                                                | 104 ms: 1.06x slower                                  |
| mako                    | 9.83 ms                                                | 10.5 ms: 1.07x slower                                 |
| hexiom                  | 6.34 ms                                                | 6.76 ms: 1.07x slower                                 |
| scimark_fft             | 325 ms                                                 | 347 ms: 1.07x slower                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 72.6 ms: 1.07x slower                                 |
| thrift                  | 760 us                                                 | 815 us: 1.07x slower                                  |
| pickle_list             | 4.14 us                                                | 4.47 us: 1.08x slower                                 |
| regex_v8                | 22.2 ms                                                | 24.0 ms: 1.08x slower                                 |
| pickle_pure_python      | 308 us                                                 | 334 us: 1.08x slower                                  |
| chameleon               | 6.38 ms                                                | 6.95 ms: 1.09x slower                                 |
| chaos                   | 68.7 ms                                                | 74.9 ms: 1.09x slower                                 |
| sqlite_synth            | 2.48 us                                                | 2.71 us: 1.09x slower                                 |
| tornado_http            | 96.5 ms                                                | 106 ms: 1.09x slower                                  |
| django_template         | 32.3 ms                                                | 35.4 ms: 1.10x slower                                 |
| unpickle_pure_python    | 227 us                                                 | 249 us: 1.10x slower                                  |
| pyflate                 | 419 ms                                                 | 459 ms: 1.10x slower                                  |
| raytrace                | 291 ms                                                 | 321 ms: 1.10x slower                                  |
| richards                | 46.1 ms                                                | 50.8 ms: 1.10x slower                                 |
| crypto_pyaes            | 75.7 ms                                                | 83.8 ms: 1.11x slower                                 |
| scimark_lu              | 108 ms                                                 | 120 ms: 1.11x slower                                  |
| scimark_sor             | 115 ms                                                 | 129 ms: 1.12x slower                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 5.14 ms: 1.12x slower                                 |
| deltablue               | 3.66 ms                                                | 4.13 ms: 1.13x slower                                 |
| logging_silent          | 98.0 ns                                                | 113 ns: 1.15x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x slower                                          |

Benchmark hidden because not significant (5): json, pickle, meteor_contest, pycparser, unpickle
Ignored benchmarks (35) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, bench_mp_pool, bench_thread_pool, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile
