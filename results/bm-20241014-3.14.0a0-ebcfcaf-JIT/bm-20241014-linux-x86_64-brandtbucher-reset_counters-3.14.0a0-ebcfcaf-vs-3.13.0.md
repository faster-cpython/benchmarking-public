# Results vs. 3.13.0

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: ebcfcaf
- commit date: 2024-10-14
- overall geometric mean: 1.02x slower
- HPT reliability: 86.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                                  |
| docutils       | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                |
| html5lib       | 64.5 ms                                                | 62.7 ms: 1.03x faster                                                 |
| tornado_http   | 91.5 ms                                                | 93.7 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp_ssl  | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                |
| asyncio_tcp      | 488 ms                                                 | 496 ms: 1.02x slower                                                  |
| coroutines       | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                 |
| async_generators | 433 ms                                                 | 454 ms: 1.05x slower                                                  |
| Geometric mean   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 72.4 ms: 1.08x faster                                                 |
| nbody          | 85.7 ms                                                | 83.5 ms: 1.03x faster                                                 |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                 |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                  |
| regex_v8       | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                 |
| regex_compile  | 131 ms                                                 | 139 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.4 ms: 1.11x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 54.9 ms: 1.10x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 102 ms                                                 | 98.0 ms: 1.04x faster                                                 |
| json_loads           | 27.0 us                                                | 26.6 us: 1.01x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                  |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| pickle_pure_python   | 300 us                                                 | 310 us: 1.03x slower                                                  |
| pickle_list          | 5.01 us                                                | 5.17 us: 1.03x slower                                                 |
| pickle_dict          | 33.2 us                                                | 35.2 us: 1.06x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| unpickle_list        | 4.96 us                                                | 5.41 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                 |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                 |
| genshi_text     | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 58.0 ms: 1.15x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-brandtbucher-reset_counters-3.14.0a0-ebcfcaf |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo            | 38.0 us                                                | 27.4 us: 1.39x faster                                                 |
| deepcopy                 | 352 us                                                 | 264 us: 1.34x faster                                                  |
| richards_super           | 54.4 ms                                                | 45.2 ms: 1.20x faster                                                 |
| deepcopy_reduce          | 3.17 us                                                | 2.66 us: 1.19x faster                                                 |
| richards                 | 48.1 ms                                                | 40.7 ms: 1.18x faster                                                 |
| scimark_fft              | 369 ms                                                 | 312 ms: 1.18x faster                                                  |
| spectral_norm            | 115 ms                                                 | 101 ms: 1.13x faster                                                  |
| xml_etree_generate       | 87.0 ms                                                | 78.4 ms: 1.11x faster                                                 |
| telco                    | 8.45 ms                                                | 7.62 ms: 1.11x faster                                                 |
| mako                     | 11.1 ms                                                | 10.0 ms: 1.11x faster                                                 |
| tomli_loads              | 2.11 sec                                               | 1.91 sec: 1.10x faster                                                |
| xml_etree_process        | 60.4 ms                                                | 54.9 ms: 1.10x faster                                                 |
| crypto_pyaes             | 73.0 ms                                                | 66.7 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult  | 5.03 ms                                                | 4.62 ms: 1.09x faster                                                 |
| float                    | 78.5 ms                                                | 72.4 ms: 1.08x faster                                                 |
| regex_effbot             | 3.88 ms                                                | 3.61 ms: 1.08x faster                                                 |
| mdp                      | 2.74 sec                                               | 2.55 sec: 1.07x faster                                                |
| pathlib                  | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                 |
| xml_etree_parse          | 156 ms                                                 | 146 ms: 1.07x faster                                                  |
| go                       | 142 ms                                                 | 132 ms: 1.07x faster                                                  |
| bpe_tokeniser            | 4.69 sec                                               | 4.39 sec: 1.07x faster                                                |
| json                     | 5.20 ms                                                | 4.93 ms: 1.05x faster                                                 |
| regex_dna                | 220 ms                                                 | 209 ms: 1.05x faster                                                  |
| regex_v8                 | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                 |
| scimark_sor              | 122 ms                                                 | 117 ms: 1.04x faster                                                  |
| scimark_monte_carlo      | 66.3 ms                                                | 63.5 ms: 1.04x faster                                                 |
| scimark_lu               | 115 ms                                                 | 110 ms: 1.04x faster                                                  |
| xml_etree_iterparse      | 102 ms                                                 | 98.0 ms: 1.04x faster                                                 |
| pycparser                | 1.19 sec                                               | 1.15 sec: 1.04x faster                                                |
| logging_format           | 6.25 us                                                | 6.04 us: 1.04x faster                                                 |
| logging_simple           | 5.66 us                                                | 5.48 us: 1.03x faster                                                 |
| html5lib                 | 64.5 ms                                                | 62.7 ms: 1.03x faster                                                 |
| pyflate                  | 460 ms                                                 | 447 ms: 1.03x faster                                                  |
| nbody                    | 85.7 ms                                                | 83.5 ms: 1.03x faster                                                 |
| logging_silent           | 102 ns                                                 | 99.8 ns: 1.02x faster                                                 |
| pprint_safe_repr         | 744 ms                                                 | 728 ms: 1.02x faster                                                  |
| pprint_pformat           | 1.51 sec                                               | 1.49 sec: 1.02x faster                                                |
| json_loads               | 27.0 us                                                | 26.6 us: 1.01x faster                                                 |
| thrift                   | 796 us                                                 | 785 us: 1.01x faster                                                  |
| sqlite_synth             | 2.85 us                                                | 2.82 us: 1.01x faster                                                 |
| python_startup           | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                 |
| pidigits                 | 186 ms                                                 | 185 ms: 1.00x faster                                                  |
| meteor_contest           | 108 ms                                                 | 107 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl          | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                |
| unpickle_pure_python     | 213 us                                                 | 215 us: 1.01x slower                                                  |
| chaos                    | 58.4 ms                                                | 59.1 ms: 1.01x slower                                                 |
| python_startup_no_site   | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                 |
| pickle                   | 11.6 us                                                | 11.8 us: 1.02x slower                                                 |
| asyncio_tcp              | 488 ms                                                 | 496 ms: 1.02x slower                                                  |
| deltablue                | 3.15 ms                                                | 3.22 ms: 1.02x slower                                                 |
| tornado_http             | 91.5 ms                                                | 93.7 ms: 1.02x slower                                                 |
| comprehensions           | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| typing_runtime_protocols | 159 us                                                 | 164 us: 1.03x slower                                                  |
| coroutines               | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                 |
| pickle_pure_python       | 300 us                                                 | 310 us: 1.03x slower                                                  |
| pickle_list              | 5.01 us                                                | 5.17 us: 1.03x slower                                                 |
| sqlglot_parse            | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                 |
| django_template          | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                 |
| 2to3                     | 265 ms                                                 | 278 ms: 1.05x slower                                                  |
| async_generators         | 433 ms                                                 | 454 ms: 1.05x slower                                                  |
| gc_traversal             | 3.81 ms                                                | 4.01 ms: 1.05x slower                                                 |
| sqlglot_transpile        | 1.57 ms                                                | 1.67 ms: 1.06x slower                                                 |
| regex_compile            | 131 ms                                                 | 139 ms: 1.06x slower                                                  |
| pickle_dict              | 33.2 us                                                | 35.2 us: 1.06x slower                                                 |
| sqlglot_normalize        | 107 ms                                                 | 114 ms: 1.06x slower                                                  |
| bench_thread_pool        | 815 us                                                 | 871 us: 1.07x slower                                                  |
| dulwich_log              | 63.0 ms                                                | 67.5 ms: 1.07x slower                                                 |
| nqueens                  | 80.6 ms                                                | 86.5 ms: 1.07x slower                                                 |
| json_dumps               | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| raytrace                 | 262 ms                                                 | 282 ms: 1.08x slower                                                  |
| sympy_expand             | 462 ms                                                 | 498 ms: 1.08x slower                                                  |
| unpickle_list            | 4.96 us                                                | 5.41 us: 1.09x slower                                                 |
| sympy_str                | 274 ms                                                 | 300 ms: 1.10x slower                                                  |
| genshi_text              | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                 |
| sqlglot_optimize         | 53.9 ms                                                | 59.3 ms: 1.10x slower                                                 |
| create_gc_cycles         | 1.61 ms                                                | 1.78 ms: 1.11x slower                                                 |
| docutils                 | 2.58 sec                                               | 2.87 sec: 1.11x slower                                                |
| hexiom                   | 6.13 ms                                                | 7.00 ms: 1.14x slower                                                 |
| genshi_xml               | 50.3 ms                                                | 58.0 ms: 1.15x slower                                                 |
| sympy_integrate          | 19.9 ms                                                | 23.2 ms: 1.17x slower                                                 |
| sympy_sum                | 150 ms                                                 | 175 ms: 1.17x slower                                                  |
| pylint                   | 313 ms                                                 | 373 ms: 1.19x slower                                                  |
| generators               | 28.8 ms                                                | 35.3 ms: 1.23x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 60.8 ms: 2.53x slower                                                 |
| unpack_sequence          | 42.4 ns                                                | 112 ns: 2.64x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (4): unpickle, coverage, asyncio_websockets, fannkuch
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 86.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x