
# Results vs. base

- fork: iritkatriel
- ref: fetch_restore
- machine: linux-x86_64
- commit hash: d83af14
- commit date: 2023-02-23
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 247 ms: 1.01x faster                                                 |
| chameleon      | 6.32 ms                                                                | 6.39 ms: 1.01x slower                                                |
| docutils       | 2.54 sec                                                               | 2.52 sec: 1.01x faster                                               |
| tornado_http   | 95.3 ms                                                                | 94.5 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.3 ms                                                                | 95.4 ms: 1.02x faster                                                |
| pidigits       | 189 ms                                                                 | 193 ms: 1.02x slower                                                 |
| float          | 72.5 ms                                                                | 73.7 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 214 ms                                                                 | 199 ms: 1.07x faster                                                 |
| regex_effbot   | 3.79 ms                                                                | 3.58 ms: 1.06x faster                                                |
| regex_v8       | 22.3 ms                                                                | 21.7 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                                 | 98.8 ms: 1.05x faster                                                |
| pickle               | 10.2 us                                                                | 9.91 us: 1.03x faster                                                |
| json_dumps           | 9.65 ms                                                                | 9.44 ms: 1.02x faster                                                |
| xml_etree_parse      | 151 ms                                                                 | 148 ms: 1.02x faster                                                 |
| pickle_pure_python   | 284 us                                                                 | 281 us: 1.01x faster                                                 |
| pickle_dict          | 30.6 us                                                                | 30.8 us: 1.00x slower                                                |
| unpickle_pure_python | 197 us                                                                 | 198 us: 1.01x slower                                                 |
| unpickle_list        | 5.02 us                                                                | 5.08 us: 1.01x slower                                                |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (5): pickle_list, xml_etree_process, xml_etree_generate, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.98 ms                                                                | 8.99 ms: 1.00x slower                                                |
| python_startup_no_site | 6.51 ms                                                                | 6.53 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 47.4 ms                                                                | 46.5 ms: 1.02x faster                                                |
| django_template | 33.4 ms                                                                | 32.9 ms: 1.02x faster                                                |
| genshi_text     | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                |
| mako            | 9.94 ms                                                                | 9.90 ms: 1.00x faster                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20230223-linux-x86_64-python-c3a178398c199038f3a0-3.12.0a5+-c3a1783 | bm-20230223-linux-x86_64-iritkatriel-fetch_restore-3.12.0a5+-d83af14 |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna               | 214 ms                                                                 | 199 ms: 1.07x faster                                                 |
| regex_effbot            | 3.79 ms                                                                | 3.58 ms: 1.06x faster                                                |
| pycparser               | 1.14 sec                                                               | 1.08 sec: 1.05x faster                                               |
| mdp                     | 2.61 sec                                                               | 2.48 sec: 1.05x faster                                               |
| xml_etree_iterparse     | 103 ms                                                                 | 98.8 ms: 1.05x faster                                                |
| logging_format          | 6.60 us                                                                | 6.33 us: 1.04x faster                                                |
| pickle                  | 10.2 us                                                                | 9.91 us: 1.03x faster                                                |
| logging_simple          | 5.96 us                                                                | 5.79 us: 1.03x faster                                                |
| regex_v8                | 22.3 ms                                                                | 21.7 ms: 1.03x faster                                                |
| coroutines              | 23.6 ms                                                                | 23.0 ms: 1.02x faster                                                |
| json_dumps              | 9.65 ms                                                                | 9.44 ms: 1.02x faster                                                |
| xml_etree_parse         | 151 ms                                                                 | 148 ms: 1.02x faster                                                 |
| sqlalchemy_imperative   | 18.1 ms                                                                | 17.8 ms: 1.02x faster                                                |
| nbody                   | 97.3 ms                                                                | 95.4 ms: 1.02x faster                                                |
| async_generators        | 416 ms                                                                 | 408 ms: 1.02x faster                                                 |
| genshi_xml              | 47.4 ms                                                                | 46.5 ms: 1.02x faster                                                |
| django_template         | 33.4 ms                                                                | 32.9 ms: 1.02x faster                                                |
| sqlglot_normalize       | 105 ms                                                                 | 103 ms: 1.02x faster                                                 |
| logging_silent          | 92.5 ns                                                                | 91.2 ns: 1.01x faster                                                |
| pprint_safe_repr        | 685 ms                                                                 | 676 ms: 1.01x faster                                                 |
| go                      | 135 ms                                                                 | 133 ms: 1.01x faster                                                 |
| meteor_contest          | 104 ms                                                                 | 103 ms: 1.01x faster                                                 |
| deltablue               | 3.18 ms                                                                | 3.15 ms: 1.01x faster                                                |
| pickle_pure_python      | 284 us                                                                 | 281 us: 1.01x faster                                                 |
| pprint_pformat          | 1.40 sec                                                               | 1.39 sec: 1.01x faster                                               |
| pathlib                 | 17.8 ms                                                                | 17.6 ms: 1.01x faster                                                |
| crypto_pyaes            | 73.3 ms                                                                | 72.5 ms: 1.01x faster                                                |
| dulwich_log             | 63.5 ms                                                                | 62.8 ms: 1.01x faster                                                |
| 2to3                    | 250 ms                                                                 | 247 ms: 1.01x faster                                                 |
| generators              | 29.7 ms                                                                | 29.4 ms: 1.01x faster                                                |
| pyflate                 | 412 ms                                                                 | 408 ms: 1.01x faster                                                 |
| tornado_http            | 95.3 ms                                                                | 94.5 ms: 1.01x faster                                                |
| docutils                | 2.54 sec                                                               | 2.52 sec: 1.01x faster                                               |
| sqlalchemy_declarative  | 137 ms                                                                 | 135 ms: 1.01x faster                                                 |
| genshi_text             | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                |
| sympy_expand            | 457 ms                                                                 | 453 ms: 1.01x faster                                                 |
| sqlglot_optimize        | 50.9 ms                                                                | 50.5 ms: 1.01x faster                                                |
| coverage                | 95.7 ms                                                                | 95.0 ms: 1.01x faster                                                |
| richards                | 41.4 ms                                                                | 41.2 ms: 1.01x faster                                                |
| sympy_integrate         | 20.6 ms                                                                | 20.4 ms: 1.01x faster                                                |
| hexiom                  | 6.10 ms                                                                | 6.07 ms: 1.01x faster                                                |
| chaos                   | 68.0 ms                                                                | 67.6 ms: 1.01x faster                                                |
| bench_thread_pool       | 792 us                                                                 | 788 us: 1.01x faster                                                 |
| asyncio_tcp             | 505 ms                                                                 | 503 ms: 1.00x faster                                                 |
| mako                    | 9.94 ms                                                                | 9.90 ms: 1.00x faster                                                |
| sympy_str               | 283 ms                                                                 | 282 ms: 1.00x faster                                                 |
| sqlglot_parse           | 1.43 ms                                                                | 1.42 ms: 1.00x faster                                                |
| python_startup          | 8.98 ms                                                                | 8.99 ms: 1.00x slower                                                |
| create_gc_cycles        | 1.47 ms                                                                | 1.47 ms: 1.00x slower                                                |
| aiohttp                 | 1.01 ms                                                                | 1.01 ms: 1.00x slower                                                |
| python_startup_no_site  | 6.51 ms                                                                | 6.53 ms: 1.00x slower                                                |
| pickle_dict             | 30.6 us                                                                | 30.8 us: 1.00x slower                                                |
| unpickle_pure_python    | 197 us                                                                 | 198 us: 1.01x slower                                                 |
| unpack_sequence         | 44.0 ns                                                                | 44.3 ns: 1.01x slower                                                |
| thrift                  | 763 us                                                                 | 768 us: 1.01x slower                                                 |
| json                    | 4.52 ms                                                                | 4.56 ms: 1.01x slower                                                |
| unpickle_list           | 5.02 us                                                                | 5.08 us: 1.01x slower                                                |
| nqueens                 | 79.2 ms                                                                | 80.1 ms: 1.01x slower                                                |
| chameleon               | 6.32 ms                                                                | 6.39 ms: 1.01x slower                                                |
| scimark_lu              | 108 ms                                                                 | 110 ms: 1.01x slower                                                 |
| sqlite_synth            | 2.60 us                                                                | 2.64 us: 1.02x slower                                                |
| pidigits                | 189 ms                                                                 | 193 ms: 1.02x slower                                                 |
| float                   | 72.5 ms                                                                | 73.7 ms: 1.02x slower                                                |
| scimark_fft             | 313 ms                                                                 | 319 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult | 4.51 ms                                                                | 4.67 ms: 1.04x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (28): djangocms, html5lib, dask, telco, deepcopy_memo, pickle_list, gunicorn, scimark_monte_carlo, sympy_sum, sqlglot_transpile, mypy2, xml_etree_process, async_tree_cpu_io_mixed, regex_compile, xml_etree_generate, gc_traversal, bench_mp_pool, scimark_sor, async_tree_io, raytrace, deepcopy, fannkuch, deepcopy_reduce, async_tree_memoization, async_tree_none, unpickle, spectral_norm, json_loads
