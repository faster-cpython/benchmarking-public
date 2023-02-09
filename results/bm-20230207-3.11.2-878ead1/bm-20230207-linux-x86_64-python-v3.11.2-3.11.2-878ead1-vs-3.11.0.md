
# Results vs. 3.11.0

- fork: python
- ref: v3.11.2
- machine: linux-x86_64
- commit hash: 878ead1
- commit date: 2023-02-07
- overall geometric mean: 1.00x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| chameleon      | 6.41 ms                                                | 6.49 ms: 1.01x slower                                  |
| docutils       | 2.60 sec                                               | 2.55 sec: 1.02x faster                                 |
| tornado_http   | 96.6 ms                                                | 96.1 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                   |
| nbody          | 95.0 ms                                                | 93.0 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 203 ms                                                 | 192 ms: 1.06x faster                                   |
| regex_v8       | 22.3 ms                                                | 21.3 ms: 1.05x faster                                  |
| regex_effbot   | 3.36 ms                                                | 3.39 ms: 1.01x slower                                  |
| regex_compile  | 136 ms                                                 | 138 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 12.5 ms: 1.02x faster                                  |
| pickle_list          | 4.17 us                                                | 4.16 us: 1.00x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.5 ms: 1.00x slower                                  |
| xml_etree_iterparse  | 103 ms                                                 | 104 ms: 1.01x slower                                   |
| unpickle_pure_python | 225 us                                                 | 228 us: 1.01x slower                                   |
| pickle               | 9.79 us                                                | 10.00 us: 1.02x slower                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (7): json_loads, unpickle_list, unpickle, pickle_dict, xml_etree_process, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 5.96 ms                                                | 5.97 ms: 1.00x slower                                  |
| python_startup         | 8.36 ms                                                | 8.47 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 22.1 ms                                                | 21.7 ms: 1.02x faster                                  |
| genshi_xml      | 52.1 ms                                                | 51.5 ms: 1.01x faster                                  |
| django_template | 32.5 ms                                                | 32.7 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pycparser               | 1.17 sec                                               | 1.11 sec: 1.06x faster                                 |
| regex_dna               | 203 ms                                                 | 192 ms: 1.06x faster                                   |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                   |
| regex_v8                | 22.3 ms                                                | 21.3 ms: 1.05x faster                                  |
| nqueens                 | 85.0 ms                                                | 83.1 ms: 1.02x faster                                  |
| nbody                   | 95.0 ms                                                | 93.0 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                  |
| docutils                | 2.60 sec                                               | 2.55 sec: 1.02x faster                                 |
| genshi_text             | 22.1 ms                                                | 21.7 ms: 1.02x faster                                  |
| logging_format          | 6.62 us                                                | 6.49 us: 1.02x faster                                  |
| coroutines              | 26.1 ms                                                | 25.6 ms: 1.02x faster                                  |
| json_dumps              | 12.7 ms                                                | 12.5 ms: 1.02x faster                                  |
| logging_simple          | 6.06 us                                                | 5.97 us: 1.02x faster                                  |
| async_tree_cpu_io_mixed | 752 ms                                                 | 740 ms: 1.02x faster                                   |
| spectral_norm           | 99.9 ms                                                | 98.4 ms: 1.02x faster                                  |
| go                      | 143 ms                                                 | 141 ms: 1.01x faster                                   |
| richards                | 46.2 ms                                                | 45.6 ms: 1.01x faster                                  |
| sqlite_synth            | 2.49 us                                                | 2.46 us: 1.01x faster                                  |
| async_tree_none         | 529 ms                                                 | 524 ms: 1.01x faster                                   |
| genshi_xml              | 52.1 ms                                                | 51.5 ms: 1.01x faster                                  |
| sympy_expand            | 472 ms                                                 | 468 ms: 1.01x faster                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 67.7 ms: 1.01x faster                                  |
| async_tree_io           | 1.31 sec                                               | 1.30 sec: 1.01x faster                                 |
| async_generators        | 359 ms                                                 | 357 ms: 1.01x faster                                   |
| chaos                   | 68.6 ms                                                | 68.2 ms: 1.01x faster                                  |
| tornado_http            | 96.6 ms                                                | 96.1 ms: 1.01x faster                                  |
| pickle_list             | 4.17 us                                                | 4.16 us: 1.00x faster                                  |
| dulwich_log             | 63.9 ms                                                | 63.7 ms: 1.00x faster                                  |
| python_startup_no_site  | 5.96 ms                                                | 5.97 ms: 1.00x slower                                  |
| bench_thread_pool       | 810 us                                                 | 812 us: 1.00x slower                                   |
| xml_etree_generate      | 76.2 ms                                                | 76.5 ms: 1.00x slower                                  |
| sqlglot_parse           | 1.37 ms                                                | 1.38 ms: 1.00x slower                                  |
| gunicorn                | 1.12 ms                                                | 1.13 ms: 1.01x slower                                  |
| sqlglot_optimize        | 53.0 ms                                                | 53.3 ms: 1.01x slower                                  |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| django_template         | 32.5 ms                                                | 32.7 ms: 1.01x slower                                  |
| deepcopy_memo           | 36.4 us                                                | 36.8 us: 1.01x slower                                  |
| deltablue               | 3.64 ms                                                | 3.68 ms: 1.01x slower                                  |
| pprint_safe_repr        | 691 ms                                                 | 697 ms: 1.01x slower                                   |
| regex_effbot            | 3.36 ms                                                | 3.39 ms: 1.01x slower                                  |
| fannkuch                | 388 ms                                                 | 392 ms: 1.01x slower                                   |
| sqlalchemy_imperative   | 18.0 ms                                                | 18.2 ms: 1.01x slower                                  |
| xml_etree_iterparse     | 103 ms                                                 | 104 ms: 1.01x slower                                   |
| deepcopy                | 344 us                                                 | 348 us: 1.01x slower                                   |
| chameleon               | 6.41 ms                                                | 6.49 ms: 1.01x slower                                  |
| unpickle_pure_python    | 225 us                                                 | 228 us: 1.01x slower                                   |
| logging_silent          | 98.5 ns                                                | 99.8 ns: 1.01x slower                                  |
| python_startup          | 8.36 ms                                                | 8.47 ms: 1.01x slower                                  |
| regex_compile           | 136 ms                                                 | 138 ms: 1.01x slower                                   |
| sqlalchemy_declarative  | 139 ms                                                 | 141 ms: 1.02x slower                                   |
| pickle                  | 9.79 us                                                | 10.00 us: 1.02x slower                                 |
| deepcopy_reduce         | 2.97 us                                                | 3.04 us: 1.02x slower                                  |
| thrift                  | 752 us                                                 | 770 us: 1.02x slower                                   |
| pylint                  | 463 ms                                                 | 475 ms: 1.03x slower                                   |
| generators              | 72.2 ms                                                | 74.1 ms: 1.03x slower                                  |
| coverage                | 101 ms                                                 | 103 ms: 1.03x slower                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.63 ms: 1.05x slower                                  |
| mdp                     | 2.62 sec                                               | 2.77 sec: 1.06x slower                                 |
| unpack_sequence         | 43.4 ns                                                | 48.8 ns: 1.12x slower                                  |
| Geometric mean          | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (30): flaskblogging, json, scimark_fft, telco, scimark_lu, scimark_sor, json_loads, unpickle_list, mako, unpickle, meteor_contest, crypto_pyaes, sympy_integrate, sympy_sum, 2to3, pyflate, bench_mp_pool, pickle_dict, xml_etree_process, sympy_str, raytrace, aiohttp, hexiom, pprint_pformat, float, pickle_pure_python, async_tree_memoization, sqlglot_transpile, xml_etree_parse, html5lib
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: mypy
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20230207-3.11.2-878ead1/bm-20230207-linux-x86_64-python-v3.11.2-3.11.2-878ead1.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal, mypy2
