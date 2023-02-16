
# Results vs. 3.11.0

- fork: iritkatriel
- ref: const_regs2
- machine: linux-x86_64
- commit hash: 1c97383
- commit date: 2023-01-17
- overall geometric mean: 1.01x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| chameleon      | 6.38 ms                                                | 6.47 ms: 1.02x slower                                              |
| docutils       | 2.60 sec                                               | 2.61 sec: 1.01x slower                                             |
| html5lib       | 64.8 ms                                                | 60.7 ms: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 74.9 ms: 1.02x faster                                              |
| pidigits       | 197 ms                                                 | 198 ms: 1.00x slower                                               |
| nbody          | 90.0 ms                                                | 96.2 ms: 1.07x slower                                              |
| Geometric mean | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 134 ms: 1.02x faster                                               |
| regex_v8       | 22.2 ms                                                | 22.6 ms: 1.02x slower                                              |
| regex_dna      | 203 ms                                                 | 210 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                              |
| unpickle_pure_python | 227 us                                                 | 205 us: 1.11x faster                                               |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                              |
| xml_etree_parse      | 160 ms                                                 | 150 ms: 1.07x faster                                               |
| pickle_pure_python   | 308 us                                                 | 299 us: 1.03x faster                                               |
| unpickle_list        | 4.99 us                                                | 4.88 us: 1.02x faster                                              |
| pickle_dict          | 31.2 us                                                | 30.7 us: 1.02x faster                                              |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| pickle_list          | 4.14 us                                                | 4.17 us: 1.01x slower                                              |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                              |
| xml_etree_process    | 53.7 ms                                                | 54.9 ms: 1.02x slower                                              |
| xml_etree_generate   | 75.9 ms                                                | 78.8 ms: 1.04x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.60 ms: 1.00x slower                                              |
| python_startup_no_site | 6.04 ms                                                | 6.13 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.8 ms: 1.08x faster                                              |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.03x faster                                              |
| django_template | 32.3 ms                                                | 34.5 ms: 1.07x slower                                              |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 505 ms: 1.75x faster                                               |
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                              |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.07 ms: 1.13x faster                                              |
| unpickle_pure_python    | 227 us                                                 | 205 us: 1.11x faster                                               |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                              |
| genshi_xml              | 51.4 ms                                                | 47.8 ms: 1.08x faster                                              |
| xml_etree_parse         | 160 ms                                                 | 150 ms: 1.07x faster                                               |
| deltablue               | 3.66 ms                                                | 3.42 ms: 1.07x faster                                              |
| unpack_sequence         | 44.5 ns                                                | 41.7 ns: 1.07x faster                                              |
| html5lib                | 64.8 ms                                                | 60.7 ms: 1.07x faster                                              |
| nqueens                 | 83.8 ms                                                | 78.9 ms: 1.06x faster                                              |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                               |
| richards                | 46.1 ms                                                | 44.4 ms: 1.04x faster                                              |
| scimark_sor             | 115 ms                                                 | 111 ms: 1.04x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                              |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.03x faster                                              |
| scimark_fft             | 325 ms                                                 | 315 ms: 1.03x faster                                               |
| pickle_pure_python      | 308 us                                                 | 299 us: 1.03x faster                                               |
| mdp                     | 2.63 sec                                               | 2.55 sec: 1.03x faster                                             |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                             |
| scimark_monte_carlo     | 68.0 ms                                                | 66.1 ms: 1.03x faster                                              |
| json                    | 4.87 ms                                                | 4.74 ms: 1.03x faster                                              |
| float                   | 76.8 ms                                                | 74.9 ms: 1.02x faster                                              |
| pyflate                 | 419 ms                                                 | 409 ms: 1.02x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                             |
| unpickle_list           | 4.99 us                                                | 4.88 us: 1.02x faster                                              |
| bench_thread_pool       | 817 us                                                 | 801 us: 1.02x faster                                               |
| regex_compile           | 136 ms                                                 | 134 ms: 1.02x faster                                               |
| pickle_dict             | 31.2 us                                                | 30.7 us: 1.02x faster                                              |
| pprint_safe_repr        | 706 ms                                                 | 697 ms: 1.01x faster                                               |
| sympy_expand            | 475 ms                                                 | 470 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| thrift                  | 760 us                                                 | 753 us: 1.01x faster                                               |
| coroutines              | 26.2 ms                                                | 26.0 ms: 1.01x faster                                              |
| hexiom                  | 6.34 ms                                                | 6.31 ms: 1.00x faster                                              |
| pidigits                | 197 ms                                                 | 198 ms: 1.00x slower                                               |
| python_startup          | 8.58 ms                                                | 8.60 ms: 1.00x slower                                              |
| sqlglot_optimize        | 52.7 ms                                                | 53.0 ms: 1.00x slower                                              |
| dulwich_log             | 64.0 ms                                                | 64.3 ms: 1.01x slower                                              |
| docutils                | 2.60 sec                                               | 2.61 sec: 1.01x slower                                             |
| pickle_list             | 4.14 us                                                | 4.17 us: 1.01x slower                                              |
| go                      | 140 ms                                                 | 141 ms: 1.01x slower                                               |
| logging_silent          | 98.0 ns                                                | 98.6 ns: 1.01x slower                                              |
| sympy_sum               | 166 ms                                                 | 168 ms: 1.01x slower                                               |
| pathlib                 | 18.1 ms                                                | 18.3 ms: 1.01x slower                                              |
| logging_format          | 6.48 us                                                | 6.57 us: 1.01x slower                                              |
| async_tree_none         | 526 ms                                                 | 534 ms: 1.01x slower                                               |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.13 ms: 1.01x slower                                              |
| chameleon               | 6.38 ms                                                | 6.47 ms: 1.02x slower                                              |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                              |
| regex_v8                | 22.2 ms                                                | 22.6 ms: 1.02x slower                                              |
| coverage                | 99.3 ms                                                | 101 ms: 1.02x slower                                               |
| spectral_norm           | 98.1 ms                                                | 100 ms: 1.02x slower                                               |
| scimark_lu              | 108 ms                                                 | 110 ms: 1.02x slower                                               |
| xml_etree_process       | 53.7 ms                                                | 54.9 ms: 1.02x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                             |
| deepcopy                | 341 us                                                 | 350 us: 1.03x slower                                               |
| regex_dna               | 203 ms                                                 | 210 ms: 1.03x slower                                               |
| raytrace                | 291 ms                                                 | 301 ms: 1.03x slower                                               |
| deepcopy_reduce         | 3.02 us                                                | 3.12 us: 1.04x slower                                              |
| xml_etree_generate      | 75.9 ms                                                | 78.8 ms: 1.04x slower                                              |
| async_tree_cpu_io_mixed | 736 ms                                                 | 765 ms: 1.04x slower                                               |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                              |
| sympy_integrate         | 21.0 ms                                                | 22.1 ms: 1.06x slower                                              |
| django_template         | 32.3 ms                                                | 34.5 ms: 1.07x slower                                              |
| async_tree_memoization  | 624 ms                                                 | 667 ms: 1.07x slower                                               |
| nbody                   | 90.0 ms                                                | 96.2 ms: 1.07x slower                                              |
| sqlglot_transpile       | 1.65 ms                                                | 1.78 ms: 1.08x slower                                              |
| sqlglot_parse           | 1.36 ms                                                | 1.48 ms: 1.08x slower                                              |
| generators              | 73.5 ms                                                | 79.9 ms: 1.09x slower                                              |
| gc_traversal            | 3.82 ms                                                | 4.29 ms: 1.12x slower                                              |
| dask                    | 365 ms                                                 | 519 ms: 1.42x slower                                               |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (13): telco, sympy_str, logging_simple, 2to3, djangocms, deepcopy_memo, bench_mp_pool, async_generators, mako, crypto_pyaes, chaos, regex_effbot, unpickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-1c97383/bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383.json: mypy
