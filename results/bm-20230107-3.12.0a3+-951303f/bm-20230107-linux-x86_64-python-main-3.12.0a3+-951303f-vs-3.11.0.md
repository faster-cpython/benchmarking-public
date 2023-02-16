
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 951303f
- commit date: 2023-01-07
- overall geometric mean: 1.02x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 255 ms: 1.02x faster                                   |
| chameleon      | 6.38 ms                                                | 6.41 ms: 1.01x slower                                  |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                 |
| html5lib       | 64.8 ms                                                | 59.7 ms: 1.09x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.8 ms: 1.06x faster                                  |
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| nbody          | 90.0 ms                                                | 96.7 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.17 ms: 1.09x faster                                  |
| regex_dna      | 203 ms                                                 | 189 ms: 1.08x faster                                   |
| regex_v8       | 22.2 ms                                                | 20.8 ms: 1.07x faster                                  |
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                  |
| pickle_pure_python   | 308 us                                                 | 284 us: 1.08x faster                                   |
| unpickle_pure_python | 227 us                                                 | 210 us: 1.08x faster                                   |
| xml_etree_parse      | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| xml_etree_process    | 53.7 ms                                                | 53.4 ms: 1.01x faster                                  |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| xml_etree_generate   | 75.9 ms                                                | 78.2 ms: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (6): unpickle, pickle_list, json_loads, xml_etree_iterparse, unpickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.51 ms: 1.01x faster                                  |
| python_startup_no_site | 6.04 ms                                                | 6.09 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.4 ms: 1.08x faster                                  |
| genshi_text     | 21.5 ms                                                | 20.7 ms: 1.04x faster                                  |
| mako            | 9.83 ms                                                | 9.54 ms: 1.03x faster                                  |
| django_template | 32.3 ms                                                | 32.9 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                  |
| deltablue               | 3.66 ms                                                | 3.25 ms: 1.12x faster                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.11 ms: 1.12x faster                                  |
| richards                | 46.1 ms                                                | 42.3 ms: 1.09x faster                                  |
| regex_effbot            | 3.46 ms                                                | 3.17 ms: 1.09x faster                                  |
| html5lib                | 64.8 ms                                                | 59.7 ms: 1.09x faster                                  |
| genshi_xml              | 51.4 ms                                                | 47.4 ms: 1.08x faster                                  |
| pickle_pure_python      | 308 us                                                 | 284 us: 1.08x faster                                   |
| unpickle_pure_python    | 227 us                                                 | 210 us: 1.08x faster                                   |
| regex_dna               | 203 ms                                                 | 189 ms: 1.08x faster                                   |
| xml_etree_parse         | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| regex_v8                | 22.2 ms                                                | 20.8 ms: 1.07x faster                                  |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                   |
| deepcopy_memo           | 35.8 us                                                | 33.6 us: 1.06x faster                                  |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.06x faster                                   |
| float                   | 76.8 ms                                                | 72.8 ms: 1.06x faster                                  |
| scimark_monte_carlo     | 68.0 ms                                                | 64.6 ms: 1.05x faster                                  |
| unpack_sequence         | 44.5 ns                                                | 42.4 ns: 1.05x faster                                  |
| pycparser               | 1.19 sec                                               | 1.13 sec: 1.05x faster                                 |
| hexiom                  | 6.34 ms                                                | 6.06 ms: 1.05x faster                                  |
| bench_thread_pool       | 817 us                                                 | 781 us: 1.05x faster                                   |
| logging_simple          | 6.02 us                                                | 5.77 us: 1.04x faster                                  |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| logging_silent          | 98.0 ns                                                | 94.1 ns: 1.04x faster                                  |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                 |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                   |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                  |
| genshi_text             | 21.5 ms                                                | 20.7 ms: 1.04x faster                                  |
| coroutines              | 26.2 ms                                                | 25.2 ms: 1.04x faster                                  |
| pprint_safe_repr        | 706 ms                                                 | 681 ms: 1.04x faster                                   |
| deepcopy                | 341 us                                                 | 330 us: 1.03x faster                                   |
| nqueens                 | 83.8 ms                                                | 81.0 ms: 1.03x faster                                  |
| raytrace                | 291 ms                                                 | 282 ms: 1.03x faster                                   |
| mako                    | 9.83 ms                                                | 9.54 ms: 1.03x faster                                  |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                   |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| logging_format          | 6.48 us                                                | 6.31 us: 1.03x faster                                  |
| fannkuch                | 384 ms                                                 | 376 ms: 1.02x faster                                   |
| sympy_str               | 291 ms                                                 | 285 ms: 1.02x faster                                   |
| sqlglot_optimize        | 52.7 ms                                                | 51.7 ms: 1.02x faster                                  |
| 2to3                    | 259 ms                                                 | 255 ms: 1.02x faster                                   |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                  |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                  |
| telco                   | 6.43 ms                                                | 6.36 ms: 1.01x faster                                  |
| python_startup          | 8.58 ms                                                | 8.51 ms: 1.01x faster                                  |
| xml_etree_process       | 53.7 ms                                                | 53.4 ms: 1.01x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 107 ms: 1.00x faster                                   |
| chameleon               | 6.38 ms                                                | 6.41 ms: 1.01x slower                                  |
| scimark_lu              | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| meteor_contest          | 104 ms                                                 | 105 ms: 1.01x slower                                   |
| python_startup_no_site  | 6.04 ms                                                | 6.09 ms: 1.01x slower                                  |
| json                    | 4.87 ms                                                | 4.92 ms: 1.01x slower                                  |
| async_tree_none         | 526 ms                                                 | 536 ms: 1.02x slower                                   |
| django_template         | 32.3 ms                                                | 32.9 ms: 1.02x slower                                  |
| crypto_pyaes            | 75.7 ms                                                | 77.2 ms: 1.02x slower                                  |
| chaos                   | 68.7 ms                                                | 70.2 ms: 1.02x slower                                  |
| sqlglot_transpile       | 1.65 ms                                                | 1.69 ms: 1.03x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                 |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                  |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 757 ms: 1.03x slower                                   |
| xml_etree_generate      | 75.9 ms                                                | 78.2 ms: 1.03x slower                                  |
| generators              | 73.5 ms                                                | 76.2 ms: 1.04x slower                                  |
| sqlite_synth            | 2.48 us                                                | 2.60 us: 1.05x slower                                  |
| nbody                   | 90.0 ms                                                | 96.7 ms: 1.07x slower                                  |
| async_tree_memoization  | 624 ms                                                 | 672 ms: 1.08x slower                                   |
| Geometric mean          | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (15): djangocms, unpickle, thrift, sympy_sum, scimark_fft, pickle_list, json_loads, mdp, bench_mp_pool, coverage, async_generators, xml_etree_iterparse, unpickle_list, spectral_norm, pickle_dict
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230107-3.12.0a3+-951303f/bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f.json: mypy
