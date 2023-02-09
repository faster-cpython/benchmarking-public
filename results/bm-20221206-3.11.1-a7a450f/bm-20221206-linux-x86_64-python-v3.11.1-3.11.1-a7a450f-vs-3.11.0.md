
# Results vs. 3.11.0

- fork: python
- ref: v3.11.1
- machine: linux-x86_64
- commit hash: a7a450f
- commit date: 2022-12-06
- overall geometric mean: 1.00x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 258 ms: 1.00x slower                                   |
| chameleon      | 6.41 ms                                                | 6.63 ms: 1.03x slower                                  |
| docutils       | 2.60 sec                                               | 2.57 sec: 1.01x faster                                 |
| tornado_http   | 96.6 ms                                                | 99.8 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_effbot   | 3.36 ms                                                | 3.31 ms: 1.01x faster                                  |
| regex_compile  | 136 ms                                                 | 137 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                  |
| pickle_dict          | 31.4 us                                                | 31.1 us: 1.01x faster                                  |
| pickle               | 9.79 us                                                | 9.72 us: 1.01x faster                                  |
| json_dumps           | 12.7 ms                                                | 12.6 ms: 1.00x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.6 ms: 1.00x slower                                  |
| xml_etree_iterparse  | 103 ms                                                 | 103 ms: 1.01x slower                                   |
| unpickle_pure_python | 225 us                                                 | 229 us: 1.01x slower                                   |
| pickle_pure_python   | 304 us                                                 | 310 us: 1.02x slower                                   |
| Geometric mean       | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_list, unpickle_list, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 5.98 ms: 1.00x slower                                  |
| python_startup         | 8.36 ms                                                | 8.49 ms: 1.02x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.85 ms                                                | 9.92 ms: 1.01x slower                                  |
| genshi_xml      | 52.1 ms                                                | 52.5 ms: 1.01x slower                                  |
| django_template | 32.5 ms                                                | 33.2 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                  |
| json                    | 4.95 ms                                                | 4.63 ms: 1.07x faster                                  |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                   |
| coroutines              | 26.1 ms                                                | 25.3 ms: 1.03x faster                                  |
| go                      | 143 ms                                                 | 140 ms: 1.03x faster                                   |
| logging_simple          | 6.06 us                                                | 5.95 us: 1.02x faster                                  |
| crypto_pyaes            | 73.9 ms                                                | 72.6 ms: 1.02x faster                                  |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_effbot            | 3.36 ms                                                | 3.31 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 752 ms                                                 | 742 ms: 1.01x faster                                   |
| logging_format          | 6.62 us                                                | 6.54 us: 1.01x faster                                  |
| docutils                | 2.60 sec                                               | 2.57 sec: 1.01x faster                                 |
| async_tree_none         | 529 ms                                                 | 523 ms: 1.01x faster                                   |
| pickle_dict             | 31.4 us                                                | 31.1 us: 1.01x faster                                  |
| fannkuch                | 388 ms                                                 | 384 ms: 1.01x faster                                   |
| sqlite_synth            | 2.49 us                                                | 2.47 us: 1.01x faster                                  |
| pickle                  | 9.79 us                                                | 9.72 us: 1.01x faster                                  |
| dulwich_log             | 63.9 ms                                                | 63.5 ms: 1.01x faster                                  |
| scimark_fft             | 329 ms                                                 | 327 ms: 1.00x faster                                   |
| json_dumps              | 12.7 ms                                                | 12.6 ms: 1.00x faster                                  |
| pyflate                 | 417 ms                                                 | 415 ms: 1.00x faster                                   |
| pprint_pformat          | 1.44 sec                                               | 1.44 sec: 1.00x faster                                 |
| gunicorn                | 1.12 ms                                                | 1.13 ms: 1.00x slower                                  |
| python_startup_no_site  | 5.96 ms                                                | 5.98 ms: 1.00x slower                                  |
| 2to3                    | 257 ms                                                 | 258 ms: 1.00x slower                                   |
| bench_thread_pool       | 810 us                                                 | 813 us: 1.00x slower                                   |
| xml_etree_generate      | 76.2 ms                                                | 76.6 ms: 1.00x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.00x slower                                   |
| mdp                     | 2.62 sec                                               | 2.64 sec: 1.01x slower                                 |
| sqlglot_optimize        | 53.0 ms                                                | 53.3 ms: 1.01x slower                                  |
| sympy_str               | 287 ms                                                 | 289 ms: 1.01x slower                                   |
| sympy_integrate         | 20.9 ms                                                | 21.0 ms: 1.01x slower                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.38 ms: 1.01x slower                                  |
| xml_etree_iterparse     | 103 ms                                                 | 103 ms: 1.01x slower                                   |
| scimark_sor             | 115 ms                                                 | 116 ms: 1.01x slower                                   |
| deltablue               | 3.64 ms                                                | 3.67 ms: 1.01x slower                                  |
| mako                    | 9.85 ms                                                | 9.92 ms: 1.01x slower                                  |
| genshi_xml              | 52.1 ms                                                | 52.5 ms: 1.01x slower                                  |
| regex_compile           | 136 ms                                                 | 137 ms: 1.01x slower                                   |
| sqlglot_transpile       | 1.66 ms                                                | 1.68 ms: 1.01x slower                                  |
| meteor_contest          | 105 ms                                                 | 106 ms: 1.01x slower                                   |
| raytrace                | 290 ms                                                 | 294 ms: 1.01x slower                                   |
| pprint_safe_repr        | 691 ms                                                 | 700 ms: 1.01x slower                                   |
| unpickle_pure_python    | 225 us                                                 | 229 us: 1.01x slower                                   |
| spectral_norm           | 99.9 ms                                                | 101 ms: 1.01x slower                                   |
| deepcopy                | 344 us                                                 | 349 us: 1.01x slower                                   |
| chaos                   | 68.6 ms                                                | 69.6 ms: 1.01x slower                                  |
| generators              | 72.2 ms                                                | 73.3 ms: 1.02x slower                                  |
| python_startup          | 8.36 ms                                                | 8.49 ms: 1.02x slower                                  |
| richards                | 46.2 ms                                                | 46.9 ms: 1.02x slower                                  |
| hexiom                  | 6.35 ms                                                | 6.46 ms: 1.02x slower                                  |
| sqlalchemy_declarative  | 139 ms                                                 | 141 ms: 1.02x slower                                   |
| thrift                  | 752 us                                                 | 765 us: 1.02x slower                                   |
| pickle_pure_python      | 304 us                                                 | 310 us: 1.02x slower                                   |
| deepcopy_memo           | 36.4 us                                                | 37.2 us: 1.02x slower                                  |
| django_template         | 32.5 ms                                                | 33.2 ms: 1.02x slower                                  |
| unpack_sequence         | 43.4 ns                                                | 44.6 ns: 1.03x slower                                  |
| tornado_http            | 96.6 ms                                                | 99.8 ms: 1.03x slower                                  |
| coverage                | 101 ms                                                 | 104 ms: 1.03x slower                                   |
| chameleon               | 6.41 ms                                                | 6.63 ms: 1.03x slower                                  |
| logging_silent          | 98.5 ns                                                | 102 ns: 1.04x slower                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.59 ms: 1.04x slower                                  |
| deepcopy_reduce         | 2.97 us                                                | 3.09 us: 1.04x slower                                  |
| Geometric mean          | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (26): pycparser, float, async_generators, pathlib, xml_etree_parse, pylint, pickle_list, unpickle_list, bench_mp_pool, nqueens, sqlalchemy_imperative, xml_etree_process, flaskblogging, regex_v8, scimark_lu, async_tree_io, sympy_sum, sympy_expand, genshi_text, scimark_monte_carlo, aiohttp, html5lib, nbody, async_tree_memoization, telco, unpickle
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221206-3.11.1-a7a450f/bm-20221206-linux-x86_64-python-v3.11.1-3.11.1-a7a450f.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
