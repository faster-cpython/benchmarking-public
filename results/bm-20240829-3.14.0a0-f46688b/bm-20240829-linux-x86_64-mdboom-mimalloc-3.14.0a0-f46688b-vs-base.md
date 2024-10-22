# Results vs. base

- fork: mdboom
- ref: mimalloc
- machine: linux-x86_64
- commit hash: f46688b
- commit date: 2024-08-29
- overall geometric mean: 1.01x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 251 ms: 1.02x faster                                      |
| html5lib       | 63.1 ms                                                               | 61.9 ms: 1.02x faster                                     |
| tornado_http   | 90.1 ms                                                               | 86.9 ms: 1.04x faster                                     |
| Geometric mean | (ref)                                                                 | 1.02x faster                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| asyncio_websockets      | 557 ms                                                                | 542 ms: 1.03x faster                                      |
| async_tree_none_tg      | 310 ms                                                                | 304 ms: 1.02x faster                                      |
| coroutines              | 23.1 ms                                                               | 23.0 ms: 1.01x faster                                     |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.83 sec: 1.02x slower                                    |
| async_tree_cpu_io_mixed | 556 ms                                                                | 569 ms: 1.02x slower                                      |
| asyncio_tcp             | 478 ms                                                                | 496 ms: 1.04x slower                                      |
| async_tree_memoization  | 394 ms                                                                | 415 ms: 1.05x slower                                      |
| async_tree_io_tg        | 901 ms                                                                | 948 ms: 1.05x slower                                      |
| async_tree_io           | 930 ms                                                                | 1.00 sec: 1.08x slower                                    |
| Geometric mean          | (ref)                                                                 | 1.02x slower                                              |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_generators, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| float          | 77.5 ms                                                               | 75.7 ms: 1.02x faster                                     |
| pidigits       | 187 ms                                                                | 185 ms: 1.01x faster                                      |
| nbody          | 84.1 ms                                                               | 89.7 ms: 1.07x slower                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.34 ms: 1.14x faster                                     |
| regex_v8       | 26.2 ms                                                               | 23.3 ms: 1.12x faster                                     |
| regex_dna      | 220 ms                                                                | 208 ms: 1.06x faster                                      |
| regex_compile  | 128 ms                                                                | 126 ms: 1.01x faster                                      |
| Geometric mean | (ref)                                                                 | 1.08x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| json_loads           | 28.6 us                                                               | 27.5 us: 1.04x faster                                     |
| json_dumps           | 10.5 ms                                                               | 10.1 ms: 1.04x faster                                     |
| tomli_loads          | 2.09 sec                                                              | 2.01 sec: 1.04x faster                                    |
| pickle_pure_python   | 301 us                                                                | 296 us: 1.02x faster                                      |
| xml_etree_parse      | 155 ms                                                                | 153 ms: 1.01x faster                                      |
| xml_etree_iterparse  | 104 ms                                                                | 103 ms: 1.01x faster                                      |
| unpickle_pure_python | 213 us                                                                | 214 us: 1.00x slower                                      |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                              |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.4 ms: 1.01x faster                                     |
| python_startup_no_site | 7.11 ms                                                               | 7.05 ms: 1.01x faster                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 11.3 ms                                                               | 10.4 ms: 1.09x faster                                     |
| django_template | 33.7 ms                                                               | 33.2 ms: 1.01x faster                                     |
| genshi_text     | 23.0 ms                                                               | 22.8 ms: 1.01x faster                                     |
| genshi_xml      | 49.5 ms                                                               | 49.1 ms: 1.01x faster                                     |
| Geometric mean  | (ref)                                                                 | 1.03x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20240829-linux-x86_64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot             | 3.81 ms                                                               | 3.34 ms: 1.14x faster                                     |
| regex_v8                 | 26.2 ms                                                               | 23.3 ms: 1.12x faster                                     |
| pycparser                | 1.20 sec                                                              | 1.08 sec: 1.11x faster                                    |
| mako                     | 11.3 ms                                                               | 10.4 ms: 1.09x faster                                     |
| pyflate                  | 474 ms                                                                | 442 ms: 1.07x faster                                      |
| json                     | 5.32 ms                                                               | 4.97 ms: 1.07x faster                                     |
| pathlib                  | 16.2 ms                                                               | 15.2 ms: 1.06x faster                                     |
| regex_dna                | 220 ms                                                                | 208 ms: 1.06x faster                                      |
| spectral_norm            | 114 ms                                                                | 108 ms: 1.05x faster                                      |
| nqueens                  | 81.3 ms                                                               | 77.9 ms: 1.04x faster                                     |
| deepcopy_reduce          | 2.72 us                                                               | 2.61 us: 1.04x faster                                     |
| json_loads               | 28.6 us                                                               | 27.5 us: 1.04x faster                                     |
| sqlglot_normalize        | 108 ms                                                                | 104 ms: 1.04x faster                                      |
| json_dumps               | 10.5 ms                                                               | 10.1 ms: 1.04x faster                                     |
| crypto_pyaes             | 72.6 ms                                                               | 69.9 ms: 1.04x faster                                     |
| tomli_loads              | 2.09 sec                                                              | 2.01 sec: 1.04x faster                                    |
| tornado_http             | 90.1 ms                                                               | 86.9 ms: 1.04x faster                                     |
| thrift                   | 771 us                                                                | 747 us: 1.03x faster                                      |
| deepcopy                 | 261 us                                                                | 253 us: 1.03x faster                                      |
| sqlglot_optimize         | 53.6 ms                                                               | 52.1 ms: 1.03x faster                                     |
| scimark_sor              | 125 ms                                                                | 122 ms: 1.03x faster                                      |
| sqlglot_parse            | 1.30 ms                                                               | 1.26 ms: 1.03x faster                                     |
| gc_traversal             | 3.72 ms                                                               | 3.62 ms: 1.03x faster                                     |
| asyncio_websockets       | 557 ms                                                                | 542 ms: 1.03x faster                                      |
| float                    | 77.5 ms                                                               | 75.7 ms: 1.02x faster                                     |
| async_tree_none_tg       | 310 ms                                                                | 304 ms: 1.02x faster                                      |
| 2to3                     | 257 ms                                                                | 251 ms: 1.02x faster                                      |
| html5lib                 | 63.1 ms                                                               | 61.9 ms: 1.02x faster                                     |
| pickle_pure_python       | 301 us                                                                | 296 us: 1.02x faster                                      |
| sympy_expand             | 455 ms                                                                | 447 ms: 1.02x faster                                      |
| scimark_lu               | 113 ms                                                                | 111 ms: 1.02x faster                                      |
| sympy_str                | 267 ms                                                                | 263 ms: 1.02x faster                                      |
| go                       | 118 ms                                                                | 116 ms: 1.01x faster                                      |
| django_template          | 33.7 ms                                                               | 33.2 ms: 1.01x faster                                     |
| python_startup           | 10.6 ms                                                               | 10.4 ms: 1.01x faster                                     |
| xml_etree_parse          | 155 ms                                                                | 153 ms: 1.01x faster                                      |
| deepcopy_memo            | 29.7 us                                                               | 29.3 us: 1.01x faster                                     |
| regex_compile            | 128 ms                                                                | 126 ms: 1.01x faster                                      |
| sqlglot_transpile        | 1.58 ms                                                               | 1.57 ms: 1.01x faster                                     |
| sympy_sum                | 147 ms                                                                | 146 ms: 1.01x faster                                      |
| pprint_safe_repr         | 704 ms                                                                | 697 ms: 1.01x faster                                      |
| typing_runtime_protocols | 158 us                                                                | 157 us: 1.01x faster                                      |
| scimark_fft              | 353 ms                                                                | 350 ms: 1.01x faster                                      |
| genshi_text              | 23.0 ms                                                               | 22.8 ms: 1.01x faster                                     |
| genshi_xml               | 49.5 ms                                                               | 49.1 ms: 1.01x faster                                     |
| fannkuch                 | 406 ms                                                                | 403 ms: 1.01x faster                                      |
| python_startup_no_site   | 7.11 ms                                                               | 7.05 ms: 1.01x faster                                     |
| pidigits                 | 187 ms                                                                | 185 ms: 1.01x faster                                      |
| xml_etree_iterparse      | 104 ms                                                                | 103 ms: 1.01x faster                                      |
| scimark_monte_carlo      | 66.5 ms                                                               | 66.1 ms: 1.01x faster                                     |
| coroutines               | 23.1 ms                                                               | 23.0 ms: 1.01x faster                                     |
| pprint_pformat           | 1.45 sec                                                              | 1.44 sec: 1.01x faster                                    |
| create_gc_cycles         | 1.74 ms                                                               | 1.74 ms: 1.00x faster                                     |
| sympy_integrate          | 19.5 ms                                                               | 19.5 ms: 1.00x faster                                     |
| meteor_contest           | 107 ms                                                                | 106 ms: 1.00x faster                                      |
| unpickle_pure_python     | 213 us                                                                | 214 us: 1.00x slower                                      |
| logging_silent           | 97.9 ns                                                               | 98.5 ns: 1.01x slower                                     |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.83 sec: 1.02x slower                                    |
| generators               | 27.7 ms                                                               | 28.2 ms: 1.02x slower                                     |
| raytrace                 | 259 ms                                                                | 264 ms: 1.02x slower                                      |
| richards                 | 46.0 ms                                                               | 47.0 ms: 1.02x slower                                     |
| logging_simple           | 5.51 us                                                               | 5.64 us: 1.02x slower                                     |
| async_tree_cpu_io_mixed  | 556 ms                                                                | 569 ms: 1.02x slower                                      |
| scimark_sparse_mat_mult  | 4.71 ms                                                               | 4.84 ms: 1.03x slower                                     |
| richards_super           | 51.7 ms                                                               | 53.5 ms: 1.03x slower                                     |
| asyncio_tcp              | 478 ms                                                                | 496 ms: 1.04x slower                                      |
| bpe_tokeniser            | 4.78 sec                                                              | 4.96 sec: 1.04x slower                                    |
| coverage                 | 85.3 ms                                                               | 89.3 ms: 1.05x slower                                     |
| async_tree_memoization   | 394 ms                                                                | 415 ms: 1.05x slower                                      |
| async_tree_io_tg         | 901 ms                                                                | 948 ms: 1.05x slower                                      |
| nbody                    | 84.1 ms                                                               | 89.7 ms: 1.07x slower                                     |
| async_tree_io            | 930 ms                                                                | 1.00 sec: 1.08x slower                                    |
| bench_thread_pool        | 780 us                                                                | 1.24 ms: 1.60x slower                                     |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                              |

Benchmark hidden because not significant (16): async_tree_cpu_io_mixed_tg, deltablue, pylint, hexiom, mdp, chaos, bench_mp_pool, xml_etree_generate, async_generators, docutils, xml_etree_process, comprehensions, telco, async_tree_memoization_tg, logging_format, async_tree_none

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x