
# Results vs. base

- fork: iritkatriel
- ref: int_float_freelist
- machine: linux-x86_64
- commit hash: 42ee27f
- commit date: 2023-02-07
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                      |
| docutils       | 2.50 sec                                                               | 2.49 sec: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 94.2 ms                                                                | 97.7 ms: 1.04x slower                                                     |
| pidigits       | 189 ms                                                                 | 203 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 130 ms                                                                 | 129 ms: 1.01x faster                                                      |
| regex_effbot   | 3.36 ms                                                                | 3.43 ms: 1.02x slower                                                     |
| regex_v8       | 21.1 ms                                                                | 21.8 ms: 1.04x slower                                                     |
| regex_dna      | 200 ms                                                                 | 213 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_list          | 4.26 us                                                                | 3.98 us: 1.07x faster                                                     |
| pickle_dict          | 32.2 us                                                                | 30.8 us: 1.04x faster                                                     |
| unpickle_list        | 5.04 us                                                                | 4.84 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 106 ms                                                                 | 102 ms: 1.04x faster                                                      |
| pickle               | 10.3 us                                                                | 9.98 us: 1.04x faster                                                     |
| json_loads           | 24.3 us                                                                | 23.7 us: 1.02x faster                                                     |
| unpickle             | 13.2 us                                                                | 13.0 us: 1.01x faster                                                     |
| pickle_pure_python   | 286 us                                                                 | 284 us: 1.01x faster                                                      |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.00x faster                                                      |
| xml_etree_process    | 53.4 ms                                                                | 53.6 ms: 1.00x slower                                                     |
| json_dumps           | 9.37 ms                                                                | 9.43 ms: 1.01x slower                                                     |
| xml_etree_generate   | 77.3 ms                                                                | 77.9 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.48 ms                                                                | 6.49 ms: 1.00x slower                                                     |
| python_startup         | 8.94 ms                                                                | 8.97 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 32.9 ms                                                                | 32.2 ms: 1.02x faster                                                     |
| mako            | 9.77 ms                                                                | 9.63 ms: 1.01x faster                                                     |
| genshi_text     | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                                     |
| genshi_xml      | 46.7 ms                                                                | 47.5 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20230130-linux-x86_64-python-c1b1f51cd1632f0b77da-3.12.0a4+-c1b1f51 | bm-20230207-linux-x86_64-iritkatriel-int_float_freelist-3.12.0a4+-42ee27f |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_list             | 4.26 us                                                                | 3.98 us: 1.07x faster                                                     |
| richards                | 43.9 ms                                                                | 41.4 ms: 1.06x faster                                                     |
| mdp                     | 2.58 sec                                                               | 2.45 sec: 1.05x faster                                                    |
| coroutines              | 25.8 ms                                                                | 24.6 ms: 1.05x faster                                                     |
| pickle_dict             | 32.2 us                                                                | 30.8 us: 1.04x faster                                                     |
| unpickle_list           | 5.04 us                                                                | 4.84 us: 1.04x faster                                                     |
| spectral_norm           | 98.3 ms                                                                | 94.4 ms: 1.04x faster                                                     |
| xml_etree_iterparse     | 106 ms                                                                 | 102 ms: 1.04x faster                                                      |
| pickle                  | 10.3 us                                                                | 9.98 us: 1.04x faster                                                     |
| unpack_sequence         | 43.4 ns                                                                | 42.1 ns: 1.03x faster                                                     |
| logging_silent          | 93.3 ns                                                                | 90.7 ns: 1.03x faster                                                     |
| scimark_sparse_mat_mult | 4.09 ms                                                                | 3.99 ms: 1.03x faster                                                     |
| json_loads              | 24.3 us                                                                | 23.7 us: 1.02x faster                                                     |
| django_template         | 32.9 ms                                                                | 32.2 ms: 1.02x faster                                                     |
| coverage                | 99.1 ms                                                                | 97.1 ms: 1.02x faster                                                     |
| logging_simple          | 5.73 us                                                                | 5.64 us: 1.02x faster                                                     |
| deepcopy_reduce         | 2.96 us                                                                | 2.91 us: 1.02x faster                                                     |
| json                    | 4.63 ms                                                                | 4.56 ms: 1.02x faster                                                     |
| pyflate                 | 400 ms                                                                 | 394 ms: 1.01x faster                                                      |
| mako                    | 9.77 ms                                                                | 9.63 ms: 1.01x faster                                                     |
| unpickle                | 13.2 us                                                                | 13.0 us: 1.01x faster                                                     |
| pathlib                 | 17.9 ms                                                                | 17.6 ms: 1.01x faster                                                     |
| gc_traversal            | 3.64 ms                                                                | 3.59 ms: 1.01x faster                                                     |
| chaos                   | 64.7 ms                                                                | 63.9 ms: 1.01x faster                                                     |
| dask                    | 501 ms                                                                 | 495 ms: 1.01x faster                                                      |
| dulwich_log             | 62.8 ms                                                                | 62.1 ms: 1.01x faster                                                     |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                                     |
| aiohttp                 | 1.00 ms                                                                | 995 us: 1.01x faster                                                      |
| genshi_text             | 20.7 ms                                                                | 20.5 ms: 1.01x faster                                                     |
| pickle_pure_python      | 286 us                                                                 | 284 us: 1.01x faster                                                      |
| regex_compile           | 130 ms                                                                 | 129 ms: 1.01x faster                                                      |
| logging_format          | 6.29 us                                                                | 6.26 us: 1.01x faster                                                     |
| sqlglot_optimize        | 51.3 ms                                                                | 51.0 ms: 1.01x faster                                                     |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.00x faster                                                      |
| docutils                | 2.50 sec                                                               | 2.49 sec: 1.00x faster                                                    |
| python_startup_no_site  | 6.48 ms                                                                | 6.49 ms: 1.00x slower                                                     |
| python_startup          | 8.94 ms                                                                | 8.97 ms: 1.00x slower                                                     |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.00x slower                                                      |
| sqlglot_normalize       | 106 ms                                                                 | 106 ms: 1.00x slower                                                      |
| xml_etree_process       | 53.4 ms                                                                | 53.6 ms: 1.00x slower                                                     |
| sympy_sum               | 156 ms                                                                 | 157 ms: 1.01x slower                                                      |
| json_dumps              | 9.37 ms                                                                | 9.43 ms: 1.01x slower                                                     |
| pprint_pformat          | 1.39 sec                                                               | 1.40 sec: 1.01x slower                                                    |
| sqlglot_parse           | 1.40 ms                                                                | 1.41 ms: 1.01x slower                                                     |
| xml_etree_generate      | 77.3 ms                                                                | 77.9 ms: 1.01x slower                                                     |
| deepcopy                | 328 us                                                                 | 331 us: 1.01x slower                                                      |
| deltablue               | 3.18 ms                                                                | 3.21 ms: 1.01x slower                                                     |
| scimark_fft             | 304 ms                                                                 | 308 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed | 751 ms                                                                 | 761 ms: 1.01x slower                                                      |
| genshi_xml              | 46.7 ms                                                                | 47.5 ms: 1.02x slower                                                     |
| scimark_lu              | 106 ms                                                                 | 108 ms: 1.02x slower                                                      |
| deepcopy_memo           | 33.6 us                                                                | 34.2 us: 1.02x slower                                                     |
| create_gc_cycles        | 1.45 ms                                                                | 1.48 ms: 1.02x slower                                                     |
| pycparser               | 1.08 sec                                                               | 1.10 sec: 1.02x slower                                                    |
| meteor_contest          | 103 ms                                                                 | 106 ms: 1.02x slower                                                      |
| regex_effbot            | 3.36 ms                                                                | 3.43 ms: 1.02x slower                                                     |
| scimark_monte_carlo     | 65.4 ms                                                                | 67.7 ms: 1.04x slower                                                     |
| crypto_pyaes            | 73.3 ms                                                                | 75.9 ms: 1.04x slower                                                     |
| regex_v8                | 21.1 ms                                                                | 21.8 ms: 1.04x slower                                                     |
| nbody                   | 94.2 ms                                                                | 97.7 ms: 1.04x slower                                                     |
| nqueens                 | 75.4 ms                                                                | 78.6 ms: 1.04x slower                                                     |
| fannkuch                | 361 ms                                                                 | 377 ms: 1.04x slower                                                      |
| regex_dna               | 200 ms                                                                 | 213 ms: 1.06x slower                                                      |
| pidigits                | 189 ms                                                                 | 203 ms: 1.07x slower                                                      |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (27): djangocms, chameleon, scimark_sor, html5lib, sqlite_synth, thrift, sympy_expand, raytrace, tornado_http, async_generators, go, bench_thread_pool, bench_mp_pool, generators, mypy, sympy_str, hexiom, asyncio_tcp, sympy_integrate, pprint_safe_repr, float, sqlglot_transpile, telco, xml_etree_parse, async_tree_io, async_tree_none, async_tree_memoization
