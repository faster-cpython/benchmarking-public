
# Results vs. base

- fork: iritkatriel
- ref: copy_consts
- machine: linux-x86_64
- commit hash: f8449d5
- commit date: 2023-01-18
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 257 ms: 1.02x slower                                               |
| chameleon      | 6.31 ms                                                                | 6.53 ms: 1.04x slower                                              |
| docutils       | 2.50 sec                                                               | 2.59 sec: 1.04x slower                                             |
| html5lib       | 59.5 ms                                                                | 61.5 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 95.0 ms                                                                | 93.4 ms: 1.02x faster                                              |
| pidigits       | 192 ms                                                                 | 190 ms: 1.02x faster                                               |
| float          | 72.1 ms                                                                | 73.5 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.60 ms                                                                | 3.41 ms: 1.05x faster                                              |
| regex_dna      | 211 ms                                                                 | 201 ms: 1.05x faster                                               |
| regex_v8       | 22.0 ms                                                                | 21.3 ms: 1.03x faster                                              |
| regex_compile  | 129 ms                                                                 | 132 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_iterparse  | 109 ms                                                                 | 103 ms: 1.05x faster                                               |
| pickle_list          | 4.07 us                                                                | 4.03 us: 1.01x faster                                              |
| pickle_dict          | 30.4 us                                                                | 30.6 us: 1.01x slower                                              |
| unpickle_pure_python | 200 us                                                                 | 201 us: 1.01x slower                                               |
| json_loads           | 23.8 us                                                                | 24.1 us: 1.01x slower                                              |
| pickle               | 10.1 us                                                                | 10.2 us: 1.02x slower                                              |
| xml_etree_process    | 53.8 ms                                                                | 54.6 ms: 1.02x slower                                              |
| xml_etree_generate   | 76.8 ms                                                                | 78.6 ms: 1.02x slower                                              |
| json_dumps           | 9.37 ms                                                                | 9.65 ms: 1.03x slower                                              |
| unpickle             | 12.9 us                                                                | 13.3 us: 1.03x slower                                              |
| pickle_pure_python   | 281 us                                                                 | 293 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                       |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.06 ms                                                                | 6.10 ms: 1.01x slower                                              |
| python_startup         | 8.50 ms                                                                | 8.56 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.78 ms                                                                | 9.67 ms: 1.01x faster                                              |
| genshi_text     | 20.2 ms                                                                | 20.8 ms: 1.03x slower                                              |
| genshi_xml      | 46.5 ms                                                                | 48.1 ms: 1.03x slower                                              |
| django_template | 32.3 ms                                                                | 33.8 ms: 1.05x slower                                              |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                       |

All benchmarks:
===============

| Benchmark              | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot           | 3.60 ms                                                                | 3.41 ms: 1.05x faster                                              |
| xml_etree_iterparse    | 109 ms                                                                 | 103 ms: 1.05x faster                                               |
| unpack_sequence        | 43.8 ns                                                                | 41.6 ns: 1.05x faster                                              |
| regex_dna              | 211 ms                                                                 | 201 ms: 1.05x faster                                               |
| regex_v8               | 22.0 ms                                                                | 21.3 ms: 1.03x faster                                              |
| pycparser              | 1.14 sec                                                               | 1.11 sec: 1.03x faster                                             |
| nbody                  | 95.0 ms                                                                | 93.4 ms: 1.02x faster                                              |
| pidigits               | 192 ms                                                                 | 190 ms: 1.02x faster                                               |
| mako                   | 9.78 ms                                                                | 9.67 ms: 1.01x faster                                              |
| pickle_list            | 4.07 us                                                                | 4.03 us: 1.01x faster                                              |
| crypto_pyaes           | 75.1 ms                                                                | 74.7 ms: 1.00x faster                                              |
| generators             | 79.3 ms                                                                | 79.0 ms: 1.00x faster                                              |
| async_generators       | 357 ms                                                                 | 358 ms: 1.00x slower                                               |
| python_startup_no_site | 6.06 ms                                                                | 6.10 ms: 1.01x slower                                              |
| python_startup         | 8.50 ms                                                                | 8.56 ms: 1.01x slower                                              |
| create_gc_cycles       | 1.45 ms                                                                | 1.46 ms: 1.01x slower                                              |
| pickle_dict            | 30.4 us                                                                | 30.6 us: 1.01x slower                                              |
| json                   | 4.66 ms                                                                | 4.70 ms: 1.01x slower                                              |
| unpickle_pure_python   | 200 us                                                                 | 201 us: 1.01x slower                                               |
| json_loads             | 23.8 us                                                                | 24.1 us: 1.01x slower                                              |
| scimark_sor            | 106 ms                                                                 | 108 ms: 1.01x slower                                               |
| logging_silent         | 93.9 ns                                                                | 95.0 ns: 1.01x slower                                              |
| meteor_contest         | 103 ms                                                                 | 104 ms: 1.01x slower                                               |
| asyncio_tcp            | 503 ms                                                                 | 511 ms: 1.02x slower                                               |
| pickle                 | 10.1 us                                                                | 10.2 us: 1.02x slower                                              |
| xml_etree_process      | 53.8 ms                                                                | 54.6 ms: 1.02x slower                                              |
| 2to3                   | 253 ms                                                                 | 257 ms: 1.02x slower                                               |
| async_tree_io          | 1.31 sec                                                               | 1.34 sec: 1.02x slower                                             |
| hexiom                 | 6.07 ms                                                                | 6.18 ms: 1.02x slower                                              |
| bench_thread_pool      | 782 us                                                                 | 797 us: 1.02x slower                                               |
| float                  | 72.1 ms                                                                | 73.5 ms: 1.02x slower                                              |
| pathlib                | 17.8 ms                                                                | 18.2 ms: 1.02x slower                                              |
| dulwich_log            | 62.0 ms                                                                | 63.4 ms: 1.02x slower                                              |
| go                     | 136 ms                                                                 | 139 ms: 1.02x slower                                               |
| regex_compile          | 129 ms                                                                 | 132 ms: 1.02x slower                                               |
| xml_etree_generate     | 76.8 ms                                                                | 78.6 ms: 1.02x slower                                              |
| sqlglot_parse          | 1.41 ms                                                                | 1.45 ms: 1.02x slower                                              |
| spectral_norm          | 96.4 ms                                                                | 99.0 ms: 1.03x slower                                              |
| nqueens                | 79.6 ms                                                                | 81.8 ms: 1.03x slower                                              |
| sqlglot_normalize      | 105 ms                                                                 | 108 ms: 1.03x slower                                               |
| chaos                  | 66.7 ms                                                                | 68.6 ms: 1.03x slower                                              |
| sqlglot_transpile      | 1.71 ms                                                                | 1.75 ms: 1.03x slower                                              |
| sqlglot_optimize       | 51.0 ms                                                                | 52.5 ms: 1.03x slower                                              |
| genshi_text            | 20.2 ms                                                                | 20.8 ms: 1.03x slower                                              |
| sympy_str              | 280 ms                                                                 | 288 ms: 1.03x slower                                               |
| sympy_sum              | 162 ms                                                                 | 167 ms: 1.03x slower                                               |
| json_dumps             | 9.37 ms                                                                | 9.65 ms: 1.03x slower                                              |
| pprint_pformat         | 1.38 sec                                                               | 1.42 sec: 1.03x slower                                             |
| deepcopy               | 331 us                                                                 | 341 us: 1.03x slower                                               |
| pyflate                | 393 ms                                                                 | 406 ms: 1.03x slower                                               |
| deepcopy_memo          | 34.0 us                                                                | 35.1 us: 1.03x slower                                              |
| mdp                    | 2.44 sec                                                               | 2.53 sec: 1.03x slower                                             |
| sympy_expand           | 453 ms                                                                 | 469 ms: 1.03x slower                                               |
| unpickle               | 12.9 us                                                                | 13.3 us: 1.03x slower                                              |
| genshi_xml             | 46.5 ms                                                                | 48.1 ms: 1.03x slower                                              |
| scimark_lu             | 107 ms                                                                 | 111 ms: 1.04x slower                                               |
| chameleon              | 6.31 ms                                                                | 6.53 ms: 1.04x slower                                              |
| html5lib               | 59.5 ms                                                                | 61.5 ms: 1.04x slower                                              |
| coroutines             | 24.7 ms                                                                | 25.6 ms: 1.04x slower                                              |
| raytrace               | 282 ms                                                                 | 293 ms: 1.04x slower                                               |
| docutils               | 2.50 sec                                                               | 2.59 sec: 1.04x slower                                             |
| pickle_pure_python     | 281 us                                                                 | 293 us: 1.04x slower                                               |
| deepcopy_reduce        | 2.88 us                                                                | 3.00 us: 1.04x slower                                              |
| deltablue              | 3.24 ms                                                                | 3.38 ms: 1.04x slower                                              |
| django_template        | 32.3 ms                                                                | 33.8 ms: 1.05x slower                                              |
| richards               | 41.9 ms                                                                | 43.8 ms: 1.05x slower                                              |
| dask                   | 491 ms                                                                 | 516 ms: 1.05x slower                                               |
| pprint_safe_repr       | 666 ms                                                                 | 700 ms: 1.05x slower                                               |
| scimark_monte_carlo    | 64.2 ms                                                                | 67.4 ms: 1.05x slower                                              |
| logging_simple         | 5.75 us                                                                | 6.06 us: 1.05x slower                                              |
| logging_format         | 6.28 us                                                                | 6.66 us: 1.06x slower                                              |
| async_tree_memoization | 622 ms                                                                 | 674 ms: 1.08x slower                                               |
| sympy_integrate        | 20.2 ms                                                                | 21.9 ms: 1.09x slower                                              |
| gc_traversal           | 3.57 ms                                                                | 4.30 ms: 1.20x slower                                              |
| Geometric mean         | (ref)                                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (14): telco, sqlite_synth, thrift, unpickle_list, coverage, bench_mp_pool, scimark_sparse_mat_mult, fannkuch, async_tree_cpu_io_mixed, djangocms, xml_etree_parse, scimark_fft, async_tree_none, mypy
